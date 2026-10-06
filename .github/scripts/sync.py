#!/usr/bin/env python3
"""Sync subscribed parent folders into child repos on push to main.

Behavior:
  - Reads .github/sync-config.yml.
  - Computes top-level folders changed between GITHUB_BEFORE and GITHUB_AFTER.
  - For each child whose subscribed folders intersect the changed set:
      * clones via its own SSH deploy key (named by `key_env`),
      * rsyncs each still-existing subscribed folder into the child (mirroring,
        including intra-folder deletions),
      * skips a subscribed folder that no longer exists in the parent (the
        child keeps its existing copy),
      * commits only if there are staged changes,
      * rebases onto the remote branch and pushes.
  - Children with no subscribed-folder changes are skipped entirely.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML not available on the runner", file=sys.stderr)
    sys.exit(1)

WORKSPACE = Path(os.environ.get("GITHUB_WORKSPACE", "."))
CONFIG_PATH = WORKSPACE / ".github" / "sync-config.yml"
ZERO_SHA = "0" * 40


def run(cmd, **kw):
    print(f"$ {' '.join(cmd)}", flush=True)
    return subprocess.run(cmd, check=True, **kw)


def changed_top_dirs(before, after):
    if before == ZERO_SHA or not before or not after:
        return None
    res = subprocess.run(
        ["git", "diff", "--name-only", before, after],
        cwd=WORKSPACE, check=True, capture_output=True, text=True,
    )
    dirs = set()
    for line in res.stdout.splitlines():
        line = line.strip()
        if not line:
            continue
        dirs.add(line.split("/", 1)[0])
    return dirs


def load_config():
    with open(CONFIG_PATH) as f:
        cfg = yaml.safe_load(f)
    return cfg.get("children", [])


def write_key(key_env):
    key = os.environ.get(key_env, "")
    if not key:
        raise RuntimeError(f"Secret '{key_env}' is empty or missing")
    keyfile = tempfile.NamedTemporaryFile("w", delete=False, suffix=".key")
    keyfile.write(key if key.endswith("\n") else key + "\n")
    keyfile.close()
    os.chmod(keyfile.name, 0o600)
    return keyfile.name


def sync_child(child, changed_dirs):
    repo = child["repo"]
    branch = child.get("branch") or "main"
    key_env = child["key_env"]
    folders = child["folders"]

    affected = [f for f in folders]
    if changed_dirs is not None:
        affected = [f for f in folders if f in changed_dirs]
    if not affected:
        print(f"[{repo}] no subscribed folders changed; skipping")
        return

    print(f"\n=== Syncing {repo} (branch {branch}) ===")
    print(f"    affected folders: {affected}")

    keyfile = write_key(key_env)
    workdir = tempfile.mkdtemp(prefix="child_")
    clone_dir = Path(workdir) / "child"

    ssh_cmd = (
        f"ssh -i {keyfile} -o IdentitiesOnly=yes "
        f"-o StrictHostKeyChecking=accept-new"
    )
    env = {**os.environ, "GIT_SSH_COMMAND": ssh_cmd}

    try:
        run(["git", "clone", "--quiet", f"git@github.com:{repo}.git",
             str(clone_dir)], env=env)
        run(["git", "checkout", branch], cwd=clone_dir, env=env)

        dirty = False
        for folder in affected:
            src = WORKSPACE / folder
            dst = clone_dir / folder
            if not src.exists():
                print(f"    [{folder}] removed in parent; keeping child's copy")
                continue
            dst.mkdir(parents=True, exist_ok=True)
            run(["rsync", "-a", "--delete",
                 str(src) + "/", str(dst) + "/"], cwd=WORKSPACE)
            dirty = True

        if not dirty:
            print(f"[{repo}] nothing to apply; skipping commit")
            return

        run(["git", "add", "-A"], cwd=clone_dir, env=env)
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"],
            cwd=clone_dir, env=env,
        )
        if diff.returncode == 0:
            print(f"[{repo}] no changes after sync; skipping commit")
            return

        sha = os.environ.get("GITHUB_AFTER", "")
        run(["git", "commit", "-m", f"chore: sync from parent @ {sha}"],
            cwd=clone_dir, env=env)

        run(["git", "pull", "--rebase", "origin", branch],
            cwd=clone_dir, env=env)
        run(["git", "push", "origin", branch], cwd=clone_dir, env=env)
        print(f"[{repo}] sync complete")
    finally:
        try:
            shutil.rmtree(workdir, ignore_errors=True)
            os.unlink(keyfile)
        except OSError:
            pass


def main():
    if not CONFIG_PATH.exists():
        print("No sync-config.yml found; nothing to do")
        return
    children = load_config()
    if not children:
        print("No children configured; nothing to do")
        return

    changed = changed_top_dirs(
        os.environ.get("GITHUB_BEFORE", ""),
        os.environ.get("GITHUB_AFTER", ""),
    )
    if changed is None:
        print("Initial push or forced push: syncing all subscribed folders")
    else:
        print(f"Changed top-level dirs: {sorted(changed)}")

    failures = 0
    for child in children:
        try:
            sync_child(child, changed)
        except subprocess.CalledProcessError as e:
            failures += 1
            print(f"[{child['repo']}] FAILED: {e}", file=sys.stderr)
        except Exception as e:
            failures += 1
            print(f"[{child['repo']}] ERROR: {e}", file=sys.stderr)

    if failures:
        print(f"\n{failures} child sync(s) failed", file=sys.stderr)
        sys.exit(1)
    print("\nAll child syncs completed")


if __name__ == "__main__":
    main()
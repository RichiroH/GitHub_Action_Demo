# GitHub_Action_Demo
The Parent repo for github action demo

## Demo comparison data

Sample files are available in `/home/runner/work/GitHub_Action_Demo/GitHub_Action_Demo/demo-data` to help demonstrate expected behavior.

- `run-a/` and `run-b/` contain two example runs with the same file structure.
- `expected/` contains a baseline that can be compared against either run.

Example comparison commands:

```bash
cd /home/runner/work/GitHub_Action_Demo/GitHub_Action_Demo
diff -ru demo-data/expected demo-data/run-a
diff -ru demo-data/expected demo-data/run-b
```

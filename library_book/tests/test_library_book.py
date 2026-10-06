from odoo.tests.common import TransactionCase


class TestLibraryBook(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.book = cls.env['library.book'].create({
            'title': 'Test Book',
            'isbn': '978-9999999999',
            'genre': 'fiction',
        })

    def test_borrow_book(self):
        self.book.action_borrow()
        self.assertEqual(self.book.state, 'borrowed')

    def test_return_book(self):
        self.book.action_borrow()
        self.book.action_return()
        self.assertEqual(self.book.state, 'available')

from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _order = 'title'

    title = fields.Char(string='Title', required=True)
    isbn = fields.Char(string='ISBN')
    author_id = fields.Many2one('res.partner', string='Author')
    publisher_id = fields.Many2one('res.partner', string='Publisher')
    publish_date = fields.Date(string='Publish Date')
    pages = fields.Integer(string='Number of Pages')
    price = fields.Monetary(string='Price', currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', string='Currency')
    genre = fields.Selection([
        ('fiction', 'Fiction'),
        ('nonfiction', 'Non-Fiction'),
        ('science', 'Science'),
        ('biography', 'Biography'),
        ('children', 'Children'),
    ], string='Genre', default='fiction')
    state = fields.Selection([
        ('available', 'Available'),
        ('borrowed', 'Borrowed'),
        ('lost', 'Lost'),
    ], string='State', default='available', tracking=True)
    synopsis = fields.Html(string='Synopsis')
    active = fields.Boolean(string='Active', default=True)

    def action_borrow(self):
        for book in self:
            book.state = 'borrowed'

    def action_return(self):
        for book in self:
            book.state = 'available'

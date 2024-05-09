from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Book in the University Library'
    _rec_name = 'name'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author')
    isbn = fields.Char(string='ISBN')
    description = fields.Text(string='Description')
    available = fields.Boolean(string='Available', default=True)
    published_date = fields.Date(string='Published Date')
    language = fields.Char(string='Language')
    genre = fields.Selection([
        ('fiction', 'Fiction'),
        ('non_fiction', 'Non-Fiction'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('science_fiction', 'Science Fiction'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('self_help', 'Self-Help'),
        ('other', 'Other')
    ], string='Genre')
    page_count = fields.Integer(string='Page Count')
    copy_count = fields.Integer(string='Number of Copies', default=1)

    member_id=fields.Many2one("library.member",string="member")

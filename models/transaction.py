from odoo import models, fields

class LibraryTransaction(models.Model):
    _name = 'library.transaction'
    _description = 'Library Transactions'

    member_id = fields.Many2one('library.member', string='Member', required=True)
    book_ids = fields.Many2many('library.book', string='Books', required=True)
    transaction_type = fields.Selection([
        ('borrow', 'Borrow'),
        ('return', 'Return')
    ], string='Transaction Type', required=True)
    transaction_date = fields.Date(string='Transaction Date', default=fields.Date.today())
    transaction_time = fields.Datetime(string='Transaction Time', default=fields.Datetime.now)

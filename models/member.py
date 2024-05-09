from odoo import models, fields

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Member of the University Library'

    GENDER_SELECTION = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    ROLE_SELECTION = [
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('staff', 'Staff')
    ]

    DEPARTMENT_SELECTION = [
        ('cse', 'CSE'),
        ('cis', 'CIS'),
        ('bba', 'BBA'),
        ('civil', 'CIVIL'),
        ('eee', 'EEE'),
        ('nfe', 'NFE')
    ]

    priority = fields.Selection([
        ('0', '0'),
        ('1', '1'),
        ('2', '2')
    ], string='Priority', default='1', widget='priority')

    memberID = fields.Integer(string='Member ID', required=True)
    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(selection=GENDER_SELECTION, string='Gender')
    role = fields.Selection(selection=ROLE_SELECTION, string='Role', required=True)
    department = fields.Selection(selection=DEPARTMENT_SELECTION, string='Department')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    status = fields.Selection([('active', 'Active'), ('inactive', 'Inactive')], string='Status', default='active')

    book_ids = fields.One2many("library.book","member_id",string="books")
    hide_author=fields.Boolean(string="hide author");
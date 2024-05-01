from odoo import api, fields, models


class LibraryMember(models.Model):
    _name="library.member"
    _description="Library User"

    name=fields.Char(string="Name")
    dept=fields.Selection([('CSE','cse'),('CIVIL','civil'),('EEE','eee')], string="Department")
    dob=fields.Date(string="Date Of Birth")




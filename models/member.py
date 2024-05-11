from odoo import api, fields, models


class LibraryMember(models.Model):
    _name="library.member"
    _description="Library User"

    name=fields.Char(string="Name")
    dept=fields.Selection([('CSE','cse'),('CIVIL','civil'),('EEE','eee')], string="Department")
    dob=fields.Date(string="Date Of Birth")
    gender=fields.Selection([('Female','female'),('Male','male')], string="Gender")
    age=fields.Integer(string="Age")
    image=fields.Image(string="image")
    color=fields.Integer(string="color")
    color2=fields.Char(string="color")
    active=fields.Boolean(string="archive", default=False)
    tags=fields.Many2many("member.tag", string="member tags")



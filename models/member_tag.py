from odoo import api, fields, models


class MemberTag(models.Model):
    _name="member.tag"
    _description="Member tag"

    name=fields.Char(string="Name")
    color=fields.Integer(string="color")
    color2=fields.Char(string="color")
    active=fields.Boolean(string="archive", default=False)



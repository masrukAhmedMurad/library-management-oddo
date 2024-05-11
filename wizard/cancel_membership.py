from odoo import api, fields, models


class LibraryMember(models.Model):
    _name="library.member.cancel"
    _description="Library User"
    tags=fields.Many2many("member.tag", string="member tags")
    reason=fields.Text(string="reason")
    def cancel_action(self):
        return

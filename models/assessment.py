from odoo import api, fields, models


class SparkAssessment(models.Model):
    _name = 'spark.assessment'
    _description = 'spark_assessment'
    name = fields.Char('Name', required=True, translate=True)
    date=fields.Date(string="Date")
    email = fields.Char('Email', required=True, translate=True)
    description=fields.Text(string="Description")
    marks=fields.Float(string="Marks")
    total_participant=fields.Integer(string="Total Participant")
    program_start_time=fields.Datetime(string="Program Start Time")
    program_end_time=fields.Datetime(string="Program End Time")
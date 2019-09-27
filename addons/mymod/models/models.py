# -*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    _name = 'ai.table'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    value3 = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
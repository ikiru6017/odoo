# -*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    _name = 'ai.table'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    value3 = fields.Text()
    group_id = fields.Many2one(comodel_name="mymod.groups")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100


class groups(models.Model):
    _name = 'mymod.groups'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    students_ids = fields.One2many(comodel_name="ai.table" , inverse_name="group_id")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
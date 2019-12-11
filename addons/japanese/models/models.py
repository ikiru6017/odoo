# -*- coding: utf-8 -*-

from odoo import models, fields, api

class students(models.Model):
    _name = 'japanese.students'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    value3 = fields.Text()
    group_id = fields.Many2one(comodel_name="japanese.groups")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100


class groups(models.Model):
    _name = 'japanese.groups'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
    students_ids = fields.One2many(comodel_name="japanese.students" , inverse_name="group_id")

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

class parts_of_speech(models.Model):
    _name = 'japanese.parts_of_speech'

    name = fields.Char()

class pole(models.Model):
    _name = 'japanese.pole'

    name = fields.Char()
    letterID = fields.Many2one(comodel_name="japanese.letters")

class stroke(models.Model):
    _name = 'japanese.stroke'

    name = fields.Char()
    letterID = fields.Many2one(comodel_name="japanese.letters")

class seito(models.Model):
    _name = 'japanese.seito'

    name = fields.Char()
    login = fields.Char()
    password = fields.Char()

class lessons(models.Model):
    _name = 'japanese.lessons'

    name = fields.Char()
    lesson_num = fields.Integer()

class task_types(models.Model):
    _name = 'japanese.task_types'

    name = fields.Char()

class letters(models.Model):
    _name = 'japanese.letters'

    strokeID = fields.One2many(comodel_name="japanese.stroke" , inverse_name="letterID")
    poleID = fields.One2many(comodel_name="japanese.pole" , inverse_name="letterID")
    title_rom = fields.Char()
    title_hira = fields.Char()
    code_hira = fields.Char()
    title_kata = fields.Char()
    code_kata = fields.Char()
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
    letterID = fields.One2many(comodel_name="japanese.letters", inverse_name="poleID")

class stroke(models.Model):
    _name = 'japanese.stroke'

    name = fields.Char()
    letterID = fields.One2many(comodel_name="japanese.letters", inverse_name="strokeID")

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

    strokeID = fields.Many2one(comodel_name="japanese.stroke")
    poleID = fields.Many2one(comodel_name="japanese.pole")
    title_rom = fields.Char()
    title_hira = fields.Char()
    code_hira = fields.Char()
    title_kata = fields.Char()
    code_kata = fields.Char()

class words(models.Model):
    _name = 'japanese.words'

    name = fields.Char()
    transcription = fields.Char()
    translation = fields.Char()
    part_of_speechID = fields.Many2one(comodel_name="japanese.parts_of_speech")
    lessonID = fields.Many2one(comodel_name="japanese.lessons")

class pronunciation(models.Model):
    _name = 'japanese.pronunciation'

    wordID = fields.Many2one(comodel_name="japanese.words")
    audiofile = fields.Char()
    
class kanji(models.Model):
    _name = 'japanese.kanji'

    name = fields.Char()
    meanings = fields.Char()
    kunyomi = fields.Char()
    onyomi = fields.Char()
    linesQty = fields.Integer()
    code = fields.Char()
    lessonID = fields.Many2one(comodel_name="japanese.lessons")

class tasks(models.Model):
    _name = 'japanese.tasks'

    lessonID = fields.Many2one(comodel_name="japanese.lessons")
    number = fields.Integer()
    part = fields.Integer()
    name = fields.Char()
    text = fields.Char()
    ans_option = fields.Char()
    typeID = fields.Many2one(comodel_name="japanese.task_types")
    image = fields.Char()
    audio = fields.Char()

class answers(models.Model):
    _name = 'japanese.answers'

    taskID = fields.Many2one(comodel_name="japanese.tasks")
    name = fields.Char()

class history(models.Model):
    _name = 'japanese.history'

    seitoID = fields.Many2one(comodel_name="japanese.seito")
    lessonID = fields.Many2one(comodel_name="japanese.lessons")
    numberID = fields.Many2one(comodel_name="japanese.tasks")
    rights = fields.Char()
    wrongs = fields.Char()
    datetime = fields.Datetime()
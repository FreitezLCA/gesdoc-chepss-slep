from odoo import api, fields, models

class Modelo(models.Model):
    _name = "nombre.modelo"
    _description = "Modelo en models"
    
    nombre = fields.Char(string='Nombre')
    rut = fields.Char(string='Rut')
    edad = fields.Integer(string='edad')
    documentos = fields.Boolean(string='Documentos')
    sexo = fields.Selection([('masculino','Masculino'),('femenino','Femenino')], string='Sexo')
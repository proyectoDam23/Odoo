# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class proyecto(models.Model):
#     _name = 'proyecto.proyecto'
#     _description = 'proyecto.proyecto'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class articulo(models.Model):
	_name = 'proyecto.articulo'
	_description = 'Articulo'

	nombre = fields.Char()
	descripcion = fields.Char()
	precio = fields.Integer()

	fotos = fields.One2many('proyecto.foto', 'articulo', string='Fotos')



class foto(models.Model):
	_name = 'proyecto.foto'
	_description = 'Foto de un articulo'

	foto = fields.Image()
	articulo = fields.Many2one("proyecto.articulo", string='articulo', ondelete='restrict')

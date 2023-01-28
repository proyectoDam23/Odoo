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

class usuario(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _description = 'Usuario de SiamrroPop'

    fecha_nacimiento = fields.Date()






class articulo(models.Model):
	_name = 'proyecto.articulo'
	_description = 'Articulo'

	name = fields.Char()
	descripcion = fields.Char()
	precio = fields.Integer()

	fotos = fields.One2many('proyecto.foto', 'articulo', string='Fotos')
	categoria = fields.Many2one("proyecto.categoria", string='Categoria', ondelete='restrict')


class foto(models.Model):
	_name = 'proyecto.foto'
	_description = 'Foto de un articulo'

	foto = fields.Image()
	articulo = fields.Many2one("proyecto.articulo", string='articulo', ondelete='restrict')

class categoria(models.Model):
	_name = 'proyecto.categoria'
	_description = 'Categorias de los Articulos'

	name = fields.Char()
	descripcion = fields.Char()
	icono = fields.Image()

	articulo = fields.One2many('proyecto.articulo', 'categoria', string='Articulos')


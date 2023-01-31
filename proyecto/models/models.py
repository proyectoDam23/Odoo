# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
	articulos_publicados = fields.One2many('proyecto.articulo', 'usuario', string='Articulos Publicados', ondelete='cascade')
	articulos_comprados = fields.One2many('proyecto.articulo', 'usuario_comprador', string='Articulos Comprados', ondelete='cascade')
	valoraciones = fields.One2many('proyecto.valoracion', 'usuario', string='Valoraciones', ondelete='cascade')
	mensajes_enviados = fields.One2many('proyecto.mensaje', 'usuario_emisor', string='Mensajes enviados', ondelete='cascade')
	mensajes_recibidos = fields.One2many('proyecto.mensaje', 'usuario_receptor', string='Mensajes recibidos', ondelete='cascade')
	
	def unlink(self):
		for u in self:
			u.articulos_publicados.unlink()
			u.articulos_comprados.unlink()
			u.valoraciones.unlink()
		return super(usuario, self).unlink()


class articulo(models.Model):
	_name = 'proyecto.articulo'
	_description = 'Articulo'

	name = fields.Char(required=True)
	descripcion = fields.Char()
	precio = fields.Float()

	fotos = fields.One2many('proyecto.foto', 'articulo', string='Fotos')
	categoria = fields.Many2one("proyecto.categoria", string='Categoria', ondelete='restrict')

	usuario = fields.Many2one("res.partner", string='Usuario', ondelete='restrict', required=True)
	usuario_comprador = fields.Many2one("res.partner", string='Comprador', ondelete='restrict')


	def unlink(self):
		for a in self:
			a.fotos.unlink()
		return super(articulo, self).unlink()


	@api.constrains('precio')
	def _precio_constraint(self):
		for record in self:
			print(record.precio)
			if record.precio < 0.1:
				raise ValidationError("El articulo debe de tener un precio.")

	@api.constrains('fotos')
	def _fotos_constraint(self):
       	 for record in self:
            if len(record.fotos)<=0:
                raise ValidationError("El articulo debe de tener una foto.")
	



class foto(models.Model):
	_name = 'proyecto.foto'
	_description = 'Foto de un articulo'

	foto = fields.Image(required=True)
	articulo = fields.Many2one("proyecto.articulo", string='articulo', ondelete='cascade')

class categoria(models.Model):
	_name = 'proyecto.categoria'
	_description = 'Categorias de los Articulos'

	name = fields.Char(required=True)
	descripcion = fields.Char(required=True)
	icono = fields.Image(required=True)

	articulo = fields.One2many('proyecto.articulo', 'categoria', string='Articulos')

class valoracion(models.Model):
	_name = 'proyecto.valoracion'
	_description = 'Valoracion de un usuario'

	valoracion = fields.Selection([('1', 'Muy Baja'),('2', 'Baja'),('3', 'Media'),('4', 'Alta'),('5', 'Muy Alta')], required=True)
	comentario = fields.Text()
	usuario = fields.Many2one("res.partner", string='Usuario', ondelete='restrict', required =True)

class mensaje(models.Model):
	_name = 'proyecto.mensaje'
	_description = 'mensajes entre usuarios'

	comentario = fields.Text()
	usuario_emisor = fields.Many2one("res.partner", string='Emisor', ondelete='restrict', required=True)
	usuario_receptor = fields.Many2one("res.partner", string='Receptor', ondelete='restrict', required=True)

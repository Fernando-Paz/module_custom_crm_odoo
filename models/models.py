# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Visit(models.Model):
     _name = 'custom_crm.visit'
     _description = 'Visit'

     name = fields.Char( String='Descripción' )
     customer = fields.Char( String='Cliente' )
     date = fields.Datetime( String='Fecha' )
     type = fields.Selection( [('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Telefonico')], string='Tipo', required=True )
     done = fields.Boolean( string='Realizada', readonly=True )


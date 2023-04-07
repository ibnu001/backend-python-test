# -*- coding: utf-8 -*-

import string
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError


class RegisterMaterial(models.Model):
    _name = 'register.material'
    _description = 'Register Material'

    m_code = fields.Char(string='Material Code', required=True)
    m_name = fields.Char(string='Material Name', required=True)
    m_type = fields.Selection([('fabric', 'Fabric'), ('jeans', 'Jeans'),('cotton', 'Cotton')], string='Material Type', required=True)
    m_buy_price = fields.Float(string='Material Buy Price', digits=(16,0), required=True)
    m_supplier_id = fields.Many2one('res.partner', string='Supplier', required=True)

    @api.constrains('m_buy_price')
    def _check_m_buy_price(self):
        for rec in self:
            if rec.m_buy_price < 100:
                raise ValidationError("Harga harus lebih besar dari 100")
         


# -*- coding: utf-8 -*-
# - Luis Felipe
from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    shop_name = fields.Char(string='Shop Name')
    shop_description = fields.Char(string='Shop Description')
    has_shop = fields.Boolean(string='Has shop?', default=False)
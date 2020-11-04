# -*- coding: utf-8 -*-
from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    @api.model
    def set_special_defaults_on_install(self):
        """ At module installation, set the default auth_signup_uninvited."""
        all_settings = self.env['res.config.settings'].search([])
        for setting in all_settings:
            setting.auth_signup_uninvited = 'b2c'


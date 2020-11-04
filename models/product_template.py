from odoo import fields, models, api


class ModelName(models.Model):
    _inherit = 'product.template'

    custom_web_published = fields.Boolean(
        string='Web published',
        default=True, )

    @api.onchange('custom_web_published')
    def _onchange_custom_web_published(self):
        self.sudo().write({'website_published': self.custom_web_published})
        #self.sudo().website_published = self.custom_web_published

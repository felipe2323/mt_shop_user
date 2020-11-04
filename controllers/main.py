# -*- coding: utf-8 -*-

import logging
from odoo import http
from odoo.http import request
from odoo.addons.auth_signup.controllers.main import AuthSignupHome

_logger = logging.getLogger(__name__)


class CustomAuthSignupHome(AuthSignupHome):

    @http.route()
    def web_auth_signup(self, *args, **kw):
        res = super(CustomAuthSignupHome, self).web_auth_signup(*args, **kw)
        qcontext = self.get_auth_signup_qcontext()
        if 'error' not in qcontext and request.httprequest.method == 'POST':
            user_id = request.env['res.users'].sudo().search([('email', '=', qcontext['login'])])
            # validation only shop active
            has_shop = qcontext.get('has_shop', False)
            if user_id and has_shop and has_shop == 'on':
                user_id.update({'shop_name': qcontext['shop_name'],
                                'shop_description': qcontext['shop_description'],
                                'has_shop': qcontext['has_shop']})
                grp_internal_xml_id = 'base.group_user'
                grp_internal = request.env.ref(grp_internal_xml_id)
                grp_portal_xml_id = 'base.group_portal'
                grp_portal = request.env.ref(grp_portal_xml_id)
                grp_public_xml_id = 'base.group_public'
                grp_public = request.env.ref(grp_public_xml_id)
                user_id.sudo().write({'sel_groups_%s_%s_%s' % (grp_internal.id, grp_portal.id, grp_public.id): grp_internal.id})
                custom_group_id = request.env.ref('mt_shop_user.group_sale_custom_vendors')
                custom_group_id.sudo().write({'users': [(4, user_id.id)]})
        return res

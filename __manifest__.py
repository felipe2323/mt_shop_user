# -*- coding: utf-8 -*-
# Copyright 2020-Present

{
    "name": "Shop for any User",
    "version": "13.0.1.0.0",
    "author": "Luis Felipe Valencia",
    "category": "Custom",
    "website": "https://www.mindtech.ml/",
    "depends": [
        "sale",
        "product",
        "stock",
        "delivery",
        "product",
        "base_setup",
        "website",
        "website_sale",
        "website_sale_stock",
        "sales_team"
    ],
    "license": "AGPL-3",
    "summary": "",
    "application": True,
    "data": [
        'data/res_config_settings.xml',
        'security/mt_secutiry.xml',
        'security/ir.model.access.csv',
        'views/res_users_view.xml',
        'views/product_view.xml',
        'views/website_templates.xml',
        'views/menu_item_view.xml',
        'views/assets.xml',
    ],
    'installable': True,
}

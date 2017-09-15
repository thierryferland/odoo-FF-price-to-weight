# -*- coding: utf-8 -*-

{
    'name': 'Point of Sale - FF Price to Weight',
    'version': '9.0.1.0.0',
    'category': 'Point Of Sale',
    'summary': 'Compute weight based on barcodes with prices in FF and product price in EUR',
    'author': 'La Récolte, TFB',
    'website': 'http://la-recolte.net/',
    'license': 'AGPL-3',
    'depends': [
        'point_of_sale',
    ],
    'data': [
        'data/barcode_rule.xml',
        'static/src/xml/templates.xml',
    ],
    'demo': [
        'demo/product_product.xml',
    ],
    'installable': True,
}

# -*- coding: utf-8 -*-

from openerp import _, api, models


class BarcodeRule(models.Model):
    _inherit = 'barcode.rule'

    @api.model
    def _get_type_selection(self):
        res = super(BarcodeRule, self)._get_type_selection()
        res.append(
            ('FF_price_to_weight', _('FF price to weight')))
        return res

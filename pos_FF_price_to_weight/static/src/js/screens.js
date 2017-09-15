
odoo.define('pos_FF_price_to_weight.screens', function (require) {
  'use strict'

  var screens = require('point_of_sale.screens')

  screens.ScreenWidget.include({
    show: function () {
      this._super()
      var self = this
      this.pos.barcode_reader.set_action_callback({
        'FF_price_to_weight': _.bind(self.barcode_product_action, self)
      })
    }
  })
})

.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===============================
Point of Sale - FF Price to Weight
===============================

This module extends Odoo Point Of Sale features, to allow to scan barcode
with price and to compute according quantity.

In Odoo by default, there are three types of barcode rules for products.

* 'Unit Product' (type='product'). Scanning a product will add a unit of this
  product to the current order.
* 'Priced product' (type='price'). A price is extracted from the barcode, and
  a new line with the given price and a quantity = 1 is added to the current
  order.
* 'Weighted product' (type='weight). A weight is extracted from the barcode,
  and a new line with the given weight, and a computed price
  (quantity * Unit price) is added to the current order.

This module add a new option:

* 'FF priced to weight' (type='FF_price_to_weight'). A price in FF is 
  extracted from the barcode, and a new line with the product price in €/Unit, and a
  computed quantity is added to the current order.


Samples

* Given a product with a unit price of 19€ / kg
* The barcode is 0212345{NNNDD}x where:
    * 02 is the prefix of the barcode rule
    * 12345 is the product number
    * {NNNDD} is the price of the scaled product in French Francs
    * x is the control digit

if {NNNDD} is 03805, the price is 38.05 FF an  and the according quantity is 
38.05 FF / 19 €/kg / 6.55957 FF/€ = 0.305 kg


Configuration
=============

* Go to 'Point of Sale' / 'Configuration' / 'Barcode Nomenclatures'
* Edit your barcode rules, according to your barcodes settings

Usage
=====

.. image:: https://odoo-community.org/website/image/ir.attachment/5784_f2813bd/datas
   :alt: Try me on Runbot
   :target: https://runbot.odoo-community.org/runbot/184/9.0


Credits
=======

Images
------

Icon parts come from https://fr.wikipedia.org

Contributors
------------

* Sylvain LE GAL <https://twitter.com/legalsylvain>
* Thierry Ferland


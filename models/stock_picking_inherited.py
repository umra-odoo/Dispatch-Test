from odoo import fields, models, api


class StockPickingInherited(models.Model):
    _inherit = "stock.picking"
    
    weight = fields.Float(related="product_id.weight", string="Weight")
    volume = fields.Float(related="product_id.volume", string="Volume")


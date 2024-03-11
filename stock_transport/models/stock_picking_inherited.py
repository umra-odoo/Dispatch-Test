from odoo import fields, models, api


class StockPickingInherited(models.Model):
    _inherit = "stock.picking"
    
    weight = fields.Float(related="product_id.weight", string="Weight", store=True)
    volume = fields.Float(related="product_id.volume", string="Volume", store=True)

    api.depends("move_ids")
    def _compute_weight(self):
        for record in self:
            if record.move_ids:
                total_weight = 0
                for line in record.move_ids:
                    total_weight += line.product_id.weight
            record.weight = total_weight

    @api.depends("move_ids")
    def _compute_volume(self):
        for record in self:
            if record.move_ids:
                total_volume = 0
                for line in record.move_ids:
                    total_volume += line.product_id.volume

            record.volume = total_volume



from odoo import fields, models, api


class StockPickingBatchInherited(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(comodel_name="dock", string="Dock Name")
    vehicle_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(comodel_name="fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight", compute="_compute_weight", readonly=True)
    volume = fields.Float(string="Volume", compute="_compute_volume", readonly=True)

    # compute methods
    def _compute_weight(self):
        tot = 0.0
        for batch in self:
            weights = batch.move_ids.product_id.mapped('weight')
            quantity = batch.move_ids.mapped('quantity')
            for i in range(0, len(weights)):
                tot += weights[i] * quantity[i]

        self.weight = tot*100 / self.vehicle_category_id.maxWeight 
    
    def _compute_volume(self):
        tot = 0.0
        for batch in self:
            volumes = batch.move_ids.product_id.mapped('volume')
            quantity = batch.move_ids.mapped('quantity')
            for i in range(0, len(volumes)):
                tot += volumes[i] * quantity[i]

        self.volume = tot*100 / self.vehicle_category_id.max_volume
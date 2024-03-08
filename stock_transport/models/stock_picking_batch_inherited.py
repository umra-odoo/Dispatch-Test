from odoo import fields, models, api


class StockPickingBatchInherited(models.Model):
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one(comodel_name="dock", string="Dock Name")
    vehicle_id = fields.Many2one(comodel_name="fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one(comodel_name="fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Float(string="Weight", compute="_compute_weight", readonly=True, store=True)
    volume = fields.Float(string="Volume", compute="_compute_volume", readonly=True, store=True)
    transfer = fields.Integer(string="Transfer", compute="_compute_transfer", store=True)
    line = fields.Integer(string="Line", compute="_compute_line", store=True)

    @api.onchange("vehicle_id")
    def update_vehicle_category(self):
        self.vehicle_category_id = self.vehicle_id.category_id

    def _compute_weight(self):
        tot = 0.0
        for batch in self:
            weights = batch.move_ids.product_id.mapped('weight')
            quantity = batch.move_ids.mapped('quantity')
            for i in range(0, len(weights)):
                tot += weights[i] * quantity[i]
        if self.vehicle_category_id.max_weight > 0:
            self.weight = tot*100 / self.vehicle_category_id.max_weight
        else:
            self.weight = 0
    
    def _compute_volume(self):
        tot = 0.0
        for batch in self:
            volumes = batch.move_ids.product_id.mapped('volume')
            quantity = batch.move_ids.mapped('quantity')
            for i in range(0, len(volumes)):
                tot += volumes[i] * quantity[i]
        if self.vehicle_category_id.max_volume > 0:
            self.volume = tot*100 / self.vehicle_category_id.max_volume
        else:
            self.volume = 0


    @api.depends("picking_ids")
    def _compute_transfer(self):
        for record in self:
            record.transfer = len(record.picking_ids)

    @api.depends("move_ids")
    def _compute_line(self):
        for record in self:
            record.line = len(record.move_ids)
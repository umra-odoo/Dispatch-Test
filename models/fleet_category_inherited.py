from odoo import fields, models, api

class FleetCategoryInherited(models.Model):
    _inherit = "fleet.vehicle.model.category"

    maxWeight = fields.Float("Max Weight (Kg)")
    max_volume = fields.Float("Max Volume (m^3)")

    @api.depends("maxWeight", "max_volume")
    def _compute_display_name(self):
        for record in self:
            name = record.name
            if record.maxWeight and record.max_volume:
                name = f"{record.name} ({record.maxWeight} Kg), ({record.max_volume} m^3)"
            record.display_name = name

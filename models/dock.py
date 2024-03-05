from odoo import fields, models, api


class Dock(models.Model):
    _name = "dock"
    _description = "Dock model"
    
    dock_name = fields.Char(string="Dock Name")

    @api.depends("dock_name")
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.dock_name
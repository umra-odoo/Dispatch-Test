from odoo import fields, models


class ResConfigSettingsInherited(models.TransientModel):
    _inherit = 'res.config.settings'

    module_transport_management = fields.Boolean("Dispatch Management System")
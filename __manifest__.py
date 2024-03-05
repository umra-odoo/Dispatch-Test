{
    'name': 'Transport Management System',
    'depends': [
        "stock_picking_batch",
        "fleet",
    ],
    'data': [
        "security/ir.model.access.csv",

        "views/fleet_category_inherited_view.xml",
        "views/dock_view.xml",
        "views/stock_picking_batch_inherited.xml",
        "views/store_picking_inhertied_view.xml",
        "views/transport_management_menus.xml",

        # "views/inventory_batch_views.xml",
        
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

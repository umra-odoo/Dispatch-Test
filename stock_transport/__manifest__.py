{
    'name': 'Stock Transport',
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
        "views/stock_transport_menus.xml",
        "views/graph_and_gantt_view.xml",
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}

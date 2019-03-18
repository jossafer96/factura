# -*- coding: utf-8 -*-



{
    'name': 'Facturas Tapices',
    'version': '1.0',
    'category': 'Hidden',
    'sequence': 2,
    'summary': 'Creacion de facturas personalizado.',
    'description': """

Este módulo agrega un equipo de ventas personalizado para que el punto de venta pueda crear una factura de formal facil.
""",
    'depends': ['point_of_sale', 'sale_management'],
    'data': [
        'data/pos_sale_data.xml',
        'security/pos_sale_security.xml',
        'security/ir.model.access.csv',
        'views/sales_team_views.xml',
        'views/pos_config_views.xml',
    ],
    'installable': True,
    'auto_install': True,
}

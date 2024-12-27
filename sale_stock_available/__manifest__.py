{
    "name": "Sale Order Stock Available",
    "version": "16.0.0.0.2",
    "author": "Valentin Romero",
    "summary": "Sale Order Stock Available",
    "website": "",
    "category": "Sale",
    "license": "AGPL-3",
    "depends": [
        "sale",
        "sale_stock",
        "stock_available_unreserved",
        "sale_stock_available_info_popup",
    ],
    "data": [
        "views/stock_quant_views.xml",
        "views/product_views.xml",
    ],
    'assets': {
        'web.assets_backend': [
            'sale_stock_available/static/src/**/*',
        ],
    },
    "installable": True,
}

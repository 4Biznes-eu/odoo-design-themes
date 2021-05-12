{
    'name': 'Bookstore Theme',
    'description': 'Books, Magazines, Music',
    'category': 'Theme/Services',
    'sequence': 250,
    'version': '1.0',
    'author': 'Odoo S.A.',
    'depends': ['theme_loftspace', 'website_animate'],
    'data': [
        'views/assets.xml',
        'views/images.xml',
        'views/preset.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'images': [
        'static/description/bookstore_description.png',
        'static/description/bookstore_screenshot.jpeg',
    ],
    'price': 4,
    'currency': 'EUR',
    'live_test_url': 'https://theme-bookstore.odoo.com'
}
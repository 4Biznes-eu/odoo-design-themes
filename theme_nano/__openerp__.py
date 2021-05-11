{
    'name': 'Nano Theme',
    'description': 'Nano Theme - Responsive Bootstrap Theme for Odoo CMS - Vertical Layout and Sidebar icons',
    'category': 'Theme/Agency',
    'sequence': 270,
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_common'],
    'data': [
        'views/assets.xml',
        'views/images_library.xml',
        'views/images_content.xml',
        'views/layout.xml',
        'views/snippets.xml',
        'views/snippets_options.xml',
        'views/customize_modal.xml',
        # STRUCTURE
        'views/snippets/s_text_image.xml',
        'views/snippets/s_image_text.xml',
        'views/snippets/s_big_picture.xml',
        # CONTENT
        'views/snippets/s_well_extended.xml',
        'views/snippets/s_quote_extended.xml',
        'views/snippets/s_panel_extended.xml',
        'views/snippets/s_separator_extended.xml',
        'views/snippets/s_share_extended.xml',
        # NANO
        'views/snippets/s_carousel_extended.xml',
        'views/snippets/s_features_circle_extended.xml',
    ],
    'demo': [
        'demo/blocks_structure.xml',
        'demo/blocks_content.xml',
        'demo/blocks_default.xml',
        'demo/blocks_features.xml',
        'demo/components.xml',
        'demo/home_01.xml',
        'demo/home_02.xml',
        'demo/home_03.xml',
    ],
    'images': [
        'static/description/nano_cover.gif',
    ],
    'price': 199,
    'currency': 'EUR',
    'live_test_url': 'https://theme-nano.odoo.com/page/demo_page_01'
}

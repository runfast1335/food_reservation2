{
    'name': 'food rezerv',
    'version': '1.0.0',
    # author: neshan dahandeye name sazandeh
    'author': 'odoo dev',
    'category': 'APP',
    # sequence: namayesh be onvane avalin app dar list
    'sequence': -101,
    # summary: yek tosif az karkarde module hast
    'summary': 'برای انتخاب غذا در طول هفته',
    'description': "",
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/days.xml',
        'views/Select.xml',
        'views/food_list.xml',
        'views/user.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets': {},

}


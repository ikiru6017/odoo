# -*- encoding: utf-8 -*-
################################################################################
#
#  This file is part of Aeroo Reports software - for license refer LICENSE file  
#
################################################################################

{
    'name': 'Aeroo Reports',
    'version': '12.0.1.0.0',
    'category': 'Generic Modules/Aeroo Reports',
    'summary': 'Enterprise grade reporting solution',
    'author': 'Alistek',
    'website': 'http://www.alistek.com',
    'complexity': "easy",
    'depends': ['base', 'web', 'mail'],
    'data': [
             "views/report_view.xml",
             "data/report_aeroo_data.xml",
             "views/webclient_report_action.xml",
             "views/report_print_by_action.xml",
             "views/installer.xml",
             "security/ir.model.access.csv"
             ],
    "license" : "GPL-3 or any later version",
    'installable': True,
    'active': False,
    'application': True,
    'auto_install': False,
}

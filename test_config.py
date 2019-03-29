from odoo.tools import config

config.get('db_name')
# 'odoo'

config.filestore(config.get('db_name'))
# /var/lib/ooo/filestore/odoo

session_path = config.session_dir
# /var/lib/odoo/sessions

parameters = config.options
# {
#     'addons_paths': '/...',
#     'db_host': 'odoo',
#     'db_filter': 'my_db',
#
#      ...
# }

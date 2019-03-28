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
#     'auto_reload': False,
#     'db_host': 'db',
#
#      ...
# }


from odoo.tools import convert

convert.str2bool('0')
# False
convert.str2bool('false')
# False
convert.str2bool('False')
# False

convert.str2bool('1')
# True
convert.str2bool('true')
# True
convert.str2bool('True')
# True

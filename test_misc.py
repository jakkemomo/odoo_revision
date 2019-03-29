from odoo.tools import misc

date_format = misc.DEFAULT_SERVER_DATE_FORMAT
# '%Y-%m-%d'
time_format = misc.DEFAULT_SERVER_TIME_FORMAT
# '%H:%M:%S'
dt_format = misc.DEFAULT_SERVER_DATETIME_FORMAT
# '%Y-%m-%d %H:%M:%S'

flat_list = misc.flatten(
    [[['a', 'b'], 'c'], 'd', [], ['e', [], 'f']])
# ['a', 'b', 'c', 'd', 'e', 'f']

for num, el in misc.reverse_enumerate(['a', 'b', 'c', 'd']):
    print(num, el)
    # 3 d
    # 2 c
    # 1 b
    # 0 a

misc.topological_sort({'a': ['b', 'c'],
                       'b': ['c'],
                       'd': ['a'],
                       'r': ['y'],
                       'y': ['z']
                       })
# ['b', 'a', 'd', 'y', 'r']


misc.scan_languages()
# [('sq_AL', 'Albanian / Shqip'),
#  ('am_ET', 'Amharic / አምሃርኛ'),
#  ('ar_SY', 'Arabic / الْعَرَبيّة'),
#  ('eu_ES', 'Basque / Euskara'),
#  ('bs_BA', 'Bosnian / bosanski jezik'),
#
#  ..]

misc.human_size(1024 * 10)
# 10.00 Kb
misc.human_size(1024 * 10000)
# 9.77 Mb
misc.human_size(1024 * 100000000)
# 95.37 Gb


for split in misc.split_every(iterable=['a', 'b', 'c', 'd'], n=2):
    print(split)
    # ('a', 'b')
    # ('c', 'd')

misc.groupby([{'first_name': 'Maris', 'last_name': 'Riediger'},
              {'first_name': 'Katya', 'last_name': 'Nikitko'},
              {'first_name': 'Zhenya', 'last_name': '1'},
              {'first_name': 'Zhenya', 'last_name': '2'},
              {'first_name': 'Zhenya', 'last_name': '3'}],
             key=lambda emp: emp['first_name'])
# dict_items([
# ('Maris', [{'first_name': 'Maris', 'last_name': 'Riediger'}]),
# ('Katya', [{'first_name': 'Katya', 'last_name': 'Nikitko'}]),
# ('Zhenya', [{'first_name': 'Zhenya', 'last_name': '1'},
#             {'first_name': 'Zhenya', 'last_name': '2'},
#             {'first_name': 'Zhenya', 'last_name': '3'}])])

print(set(misc.unique(['zhenya', 'katya', 'maris', 'zhenya', 'zhenya'])))
# ['maris', 'katya', 'zhenya']

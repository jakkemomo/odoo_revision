from dateutil.relativedelta import relativedelta
from odoo.tools import date_utils
from odoo.fields import Datetime

today = Datetime.today()
# today = datetime.strptime('2019-03-29 01:53:48', misc.DEFAULT_SERVER_DATETIME_FORMAT)
# Представим, что сейчас 2019-03-29 01:53:48

date_utils.get_month(today)
# (datetime.datetime(2019, 3, 1, 0, 0), datetime.datetime(2019, 3, 31, 0, 0))
date_utils.get_quarter(today)
# (datetime.datetime(2019, 1, 1, 0, 0), datetime.datetime(2019, 3, 31, 0, 0))
date_utils.get_quarter_number(today)
# 1
date_utils.get_fiscal_year(today)
# (datetime.datetime(2019, 1, 1, 0, 0), datetime.datetime(2019, 12, 31, 0, 0))

date_utils.start_of(today, 'hour')
# 2019-03-29 01:00:00
date_utils.start_of(today, 'day')
# 2019-03-29 00:00:00
date_utils.start_of(today, 'week')
# 2019-03-25 00:00:00
date_utils.start_of(today, 'month')
# 2019-03-01 00:00:00
date_utils.start_of(today, 'quarter')
# 2019-01-01 00:00:00
date_utils.start_of(today, 'year')
# 2019-01-01 00:00:00

date_utils.end_of(today, 'hour')
# 2019-03-29 01:59:59.999999
date_utils.end_of(today, 'day')
# 2019-03-29 23:59:59.999999
date_utils.end_of(today, 'week')
# 2019-03-31 23:59:59.999999
date_utils.end_of(today, 'month')
# 2019-03-31 23:59:59.999999
date_utils.end_of(today, 'quarter')
# 2019-03-31 23:59:59.999999
date_utils.end_of(today, 'year')
# 2019-12-31 23:59:59.999999

for date in date_utils.date_range(start=today, end=date_utils.add(today, days=15), step=relativedelta(days=1)):
    print(date)
# 2019-03-29 01:53:48
# 2019-03-30 01:53:48
# 2019-03-31 01:53:48
# 2019-04-01 01:53:48
# 2019-04-02 01:53:48
# 2019-04-03 01:53:48
# 2019-04-04 01:53:48
# 2019-04-05 01:53:48
# 2019-04-06 01:53:48
# 2019-04-07 01:53:48
# 2019-04-08 01:53:48
# 2019-04-09 01:53:48
# 2019-04-10 01:53:48
# 2019-04-11 01:53:48
# 2019-04-12 01:53:48
# 2019-04-13 01:53:48


date_utils.add(today, days=5)
# 2019-04-03 01:53:48
date_utils.add(today, weeks=2)
# 2019-04-12 01:53:48
date_utils.add(today, months=1)
# 2019-04-29 01:53:48
date_utils.add(today, years=1)
# 2020-03-29 01:53:48
date_utils.add(today, days=2, months=6, years=1)
# 2020-10-01 01:53:48


date_utils.subtract(today, days=5)
# 2019-03-24 01:53:48
date_utils.subtract(today, weeks=2)
# 2019-03-15 01:53:48
date_utils.subtract(today, months=1)
# 2019-02-28 01:53:48
date_utils.subtract(today, years=1)
# 2018-03-29 01:53:48
date_utils.subtract(today, days=2, months=6, years=1)
# 2017-09-27 01:53:48


'''
json_default()
Properly serializes date and datetime objects.
    @api.one
    @api.depends('payment_move_line_ids.amount_residual')
    def _get_payment_info_JSON(self):
        self.payments_widget = json.dumps(False)
        if self.payment_move_line_ids:
            info = {'title': _('Less Payment'), 'outstanding': False, 'content': self._get_payments_vals()}
            self.payments_widget = json.dumps(info, default=date_utils.json_default)
'''

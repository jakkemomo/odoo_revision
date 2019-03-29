from odoo.tools import float_utils

float_utils.float_round(
    1.5424,
    precision_digits=3,
    rounding_method='DOWN'
)
# 1.542

float_utils.float_round(
    1.5424,
    precision_digits=3,
    rounding_method='UP'
)

float_utils.float_round(
    1.5424,
    precision_digits=3,
    rounding_method='HALF-UP'
)
# 1.542

float_utils.float_round(
    49,
    precision_rounding=100,
    rounding_method='HALF-UP'
)
# 0.0

float_utils.float_round(
    50,
    precision_rounding=100,
    rounding_method='HALF-UP'
)
# 100.0

float_utils.float_is_zero(0.04252, precision_digits=5)
# False
float_utils.float_is_zero(0.04252, precision_digits=1)
# True

float_utils.float_compare(0.042555, 0.04256, precision_digits=5)
# 0 => Равны

float_utils.float_compare(0.042555, 0.04256, precision_digits=6)
# -1 => Первое меньше второго

float_utils.float_compare(0.04256, 0.042555, precision_digits=6)
# 1 => Первое больше второго

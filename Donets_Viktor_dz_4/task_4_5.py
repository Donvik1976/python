# *(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен
# работать и из консоли. Например:
# > python task_4_5.py USD
# 75.18, 2020-09-05

import sys
from task_4_3 import currency_rates_adv


x = sys.argv[1]
currency_rates_adv(x)


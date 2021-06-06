import datetime

from BusinessHours import BusinessHours as bh
import numpy as np
import pandas as pd
# datetime(year, month, day, hour, minute, second)
a = datetime.datetime(2021, 5, 31, 6, 0, 0)
b = datetime.datetime(2021, 6, 4, 13, 0, 0)

# returns a timedelta object
c = a - b
print('Difference: ', c)
print(c.total_seconds()/3600)


# minutes = c.total_seconds() / 60
# print('Total difference in minutes: ', minutes)
#
# # returns the difference of the time of the day
# minutes = c.seconds / 60
# print('Difference in minutes: ', minutes)
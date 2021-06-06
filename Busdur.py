import datetime

from business_duration import businessDuration
import pandas as pd

# start_date = pd.to_datetime('2021-06-03 00:00:00')
# end_date = pd.to_datetime('2021-06-18 15:00:00')
# end_date=pd.to_datetime(datetime.datetime.now())
# unit_hour='hour'
# print(businessDuration(startdate=start_date,enddate=end_date,starttime=biz_open_time,endtime=biz_close_time,unit=unit_hour))
# print(businessDuration(startdate=start_date,enddate=end_date,unit=unit_hour))


# biz_open_time=time(0,0,0)
#
# biz_close_time=time(23,0,0)


def totalHours(start__date,end__date):
    start__tsp=pd.to_datetime(start__date)
    end__tsp=pd.to_datetime(end__date)
    unit_hour='hour'
    return (businessDuration(startdate=start__tsp,enddate=end__tsp,unit=unit_hour))


print(totalHours('2021-06-03 01:00:00',datetime.datetime.now()))
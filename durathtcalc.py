import datetime
import calendar
from operator import mod

import pandas as p

# def findDay(date):
#      day=datetime.datetime.strptime(date,'%d %m %Y').weekday()
#      return (calendar.day_name[day])

 # date= '06 06 2021'
 # print(findDay(date))
 #
 # days_of_week={'Monday':18,'Tuesday':24,'Wednesday':24,'Thursday':24,'Friday':11,'Saturday':0,'Sunday':0}
 # days_list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']






# //for given start and end timestamp --> we have to
#     1.convert it to corresponding days
#     2.alter monday's and friday's hrs based on given time


tsp1=p.Timestamp(year=2021,month=6,day=4,hour=4,minute=32,second=32)
tsp2=p.Timestamp(year=2021,month=6,day=4,hour=16,minute=40,second=32)
print(tsp1)
print(tsp2)
day1=tsp1.weekday()
day2=tsp2.weekday()
dayw1=calendar.day_name[day1]
dayw2=calendar.day_name[day2]
print(dayw1)
print(dayw2)


# days_dict={'Monday':18,'Tuesday':24,'Wednesday':24,'Thursday':24,'Friday':13,'Saturday':0,'Sunday':0}
# if((dayw1.__eq__('Monday')and(dayw2.__eq__('Monday')))):
#     # mon_val=tsp1.hour+days_dict['Monday']
#     mon_val=tsp2.hour-tsp1.hour-(6-tsp1.hour)
#     print(mon_val)
#     print('TRUEE')
# else:
#     print(('FALSEE'))
#
#
# if((dayw1.__eq__('Friday')and(dayw2.__eq__('Friday')))):
#     if(tsp2.hour>=13):
#         tsphr=13
#     fri_val=tsphr-tsp1.hour
#     print(fri_val)
#
#
# if((dayw1.__eq__('Monday'))):
#     if((tsp1.hour<6)):
#         tsphr=6
#         mon_upd=tsphr+tsp1.hour


days_dict={'Monday':6,'Tuesday':24,'Wednesday':24,'Thursday':24,'Friday':11,'Saturday':0,'Sunday':0}
#if timestamp on monday registered before 6AM - calculation of hours should start from 6AM
#if timestamp on friday registered after 1PM-calculation of hours should end by 1PM
#If timestamp registered on same day, additional hours must be calculated from previous timestamp







import datetime
import time

## current date time
current_dt=datetime.datetime.now()
print(current_dt)
# current_dt_today=datetime.datetime.today()
# print(current_dt_today)

# print(current_dt.year)
# print(current_dt.month)
# print(current_dt.day)
# print(current_dt.hour)
# print(current_dt.minute)
# print(current_dt.second)
# print(current_dt.microsecond)
# print(current_dt.min)
# print(current_dt.max)


# curr_dt= datetime.datetime(2021,10,14)
# print(curr_dt)

## strftime, strptime
"""
Directive	Meaning	Example
%a	Abbreviated weekday name.	Sun, Mon, ...
%A	Full weekday name.	Sunday, Monday, ...
%w	Weekday as a decimal number.	0, 1, ..., 6
%d	Day of the month as a zero-padded decimal.	01, 02, ..., 31
%-d	Day of the month as a decimal number.	1, 2, ..., 30
%b	Abbreviated month name.	Jan, Feb, ..., Dec
%B	Full month name.	January, February, ...
%m	Month as a zero-padded decimal number.	01, 02, ..., 12
%-m	Month as a decimal number.	1, 2, ..., 12
%y	Year without century as a zero-padded decimal number.	00, 01, ..., 99
%-y	Year without century as a decimal number.	0, 1, ..., 99
%Y	Year with century as a decimal number.	2013, 2019 etc.
%H	Hour (24-hour clock) as a zero-padded decimal number.	00, 01, ..., 23
%-H	Hour (24-hour clock) as a decimal number.	0, 1, ..., 23
%I	Hour (12-hour clock) as a zero-padded decimal number.	01, 02, ..., 12
%-I	Hour (12-hour clock) as a decimal number.	1, 2, ... 12
%p	Locale’s AM or PM.	AM, PM
%M	Minute as a zero-padded decimal number.	00, 01, ..., 59
%-M	Minute as a decimal number.	0, 1, ..., 59
%S	Second as a zero-padded decimal number.	00, 01, ..., 59
%-S	Second as a decimal number.	0, 1, ..., 59
%f	Microsecond as a decimal number, zero-padded on the left.	000000 - 999999
%z	UTC offset in the form +HHMM or -HHMM.	 
%Z	Time zone name.	 
%j	Day of the year as a zero-padded decimal number.	001, 002, ..., 366
%-j	Day of the year as a decimal number.	1, 2, ..., 366
%U	Week number of the year (Sunday as the first day of the week). All days in a new year preceding the first Sunday are considered to be in week 0.	00, 01, ..., 53
%W	Week number of the year (Monday as the first day of the week). All days in a new year preceding the first Monday are considered to be in week 0.	00, 01, ..., 53
%c	Locale’s appropriate date and time representation.	Mon Sep 30 07:06:05 2013
%x	Locale’s appropriate date representation.	09/30/13
%X	Locale’s appropriate time representation.	07:06:05
%%	A literal '%' character.	%

"""

# print(current_dt.strftime("%d/%m/%Y"))
# print(current_dt.strftime("%d/%m/%Y, %H:%M:%S"))
# print(current_dt.strftime("%A")) ##

# dd= current_dt.strptime("2021/10/14","%Y/%m/%d").strftime("%d %b %Y")
# print(dd)

#============================== Time
# import time
# time_value = time.time() # 1634180000
# print(time_value)
# print(time.asctime((2021,10,14,)))
# print(time.localtime(1634180000))
# print(time.clock())
#print(current_dt.utcnow())



def sqt():
    lst =[]
    for i in range(10):
        # time.sleep(1)
        lst.append(i*i)
    print(lst[0:10])

##
# string_time= time.time()
# print("starting time",string_time)
# sqt()
# print("ending time",time.time()-string_time)

# from datetime import timedelta
# # print(timedelta(2021))
# import calendar
#
# print(calendar.MONDAY)
#
# yy = 2021
# mm = 10
# dd=14
#
# # display the calendar
# print(calendar.month(yy,mm))
# print(calendar.calendar(2018, 2, 1, 6))

# from datetime import date
# f_date = date(2014, 7, 2)
# l_date = date(2014, 7, 11)
# delta = l_date - f_date
# print(delta.days)


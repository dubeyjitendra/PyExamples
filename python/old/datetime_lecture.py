import datetime
import time


# current date time
t=datetime.datetime.today()
#print(t)
#print(datetime.datetime.now())
# Day and week day Print
#print(t.date())
#print(t.day)
#print(t.weekday())
#print(t.min) # Min
#print(t.max) # Max
#print(t.year) # Year
#print(t.month) # Month
#print(t.minute) # Min
#print(t.hour)
#print(t.microsecond) #microsecond
#print(t.microsecond)

#print(datetime.datetime.utcnow()) # UTC

#values=datetime.datetime.tzinfo

#for i in datetime.tzinfo(time.time()):
#    print(i)

#print(t.strftime("%H :%M"))


# fromtimestamp give you the date and time in local time

#your_timestamp = 1331856000000
#your_timestamp=1534308420
#date = datetime.datetime.fromtimestamp(your_timestamp)
#utcdate = datetime.datetime.utcfromtimestamp(your_timestamp)
#ord=datetime.datetime.fromordinal(t.date().toordinal())
#print("LOCAL TIME {} " .format(date))
#print("UTC TIME {}  " .format(utcdate))
#print("ordinal {}  " .format(ord))
## Second
#today = date.fromtimestamp(time.time())
#print(today)


# Install pytz then start using timeZone
#from datetime import datetime, timedelta
#from pytz import timezone
#import pytz
#amsterdam = timezone('Europe/Amsterdam')
#print(amsterdam.zone)

# New in version 3.6: Added the fold argument.
#datetime.fold # this is avaliable on grether than 3.6 version


# Time Functions

#tt=time.time()
#print(tt)
# Convert a time expressed in seconds since the epoch to a string representing local time. If secs is not provided or None, the current time as returned by time() is used. ctime(secs) is equivalent to asctime(localtime(secs)). Locale information is not used by ctime().
#print(time.ctime(tt))
# Convert a time expressed in seconds since the epoch to a struct_time in UTC in which the dst flag is always zero. If secs is not provided or None, the current time as returned by time() is used. Fractions of a second are ignored. See above for a description of the struct_time object. See calendar.timegm() for the inverse of this function.
#print(time.gmtime(tt)) # GMT + 5:30
#print(time.localtime(tt))  # IST (localtime)
#time.sleep(10)
#print('Hii')
#print(time.clock())
# altzone (DST (daylight saving time) seconds west of UTC)
#print(time.altzone)

# time delta
# With timedelta objects, you can estimate the time for both future and the past. In other words, it is a timespan to predict any special day, date or time.
#
# Remember this function is not for printing out the time or date, but something to CALCULATE about the future or past. Let's see an example to understand it better.
#print(datetime.timedelta(days=365,hours=11,minutes=25))


# dd/MM/yyyy
#print(str(t.day) + "/"+ str(t.month) + "/" + str(t.year))
#print(t.strftime("%d/%m/%Y %I:%M:%S"))
#print(t.strftime("%A"))

# Strftime() List
'''%a − abbreviated weekday name

%A − full weekday name

%b − abbreviated month name

%B − full month name

%c − preferred date and time representation

%C − century number (the year divided by 100, range 00 to 99)

%d − day of the month (01 to 31)

%D − same as %m/%d/%y

%e − day of the month (1 to 31)

%g − like %G, but without the century

%G − 4-digit year corresponding to the ISO week number (see %V).

%h − same as %b

%H − hour, using a 24-hour clock (00 to 23)

%I − hour, using a 12-hour clock (01 to 12)

%j − day of the year (001 to 366)

%m − month (01 to 12)

%M − minute

%n − newline character

%p − either am or pm according to the given time value

%r − time in a.m. and p.m. notation

%R − time in 24 hour notation

%S − second

%t − tab character

%T − current time, equal to %H:%M:%S

%u − weekday as a number (1 to 7), Monday=1. Warning: In Sun Solaris Sunday = 1

%U − week number of the current year, starting with the first Sunday as the first day of the first week

%V − The ISO 8601 week number of the current year (01 to 53), where week 1 is the first week that has at least 4 days in the current year, and with Monday as the first day of the week

%W − week number of the current year, starting with the first Monday as the first day of the first week

%w − day of the week as a decimal, Sunday = 0

%x − preferred date representation without the time

%X − preferred time representation without the date

%y − year without a century (range 00 to 99)

%Y − year including the century

%Z or %z − time zone or name or abbreviation

%% − a literal % character'''

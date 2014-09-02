import datetime;
import dateutil.rrule


date_1 = datetime.date(2014, 8, 25)
date_2 = datetime.date(2014, 9,  7)

for dt in dateutil.rrule.rrule(dateutil.rrule.DAILY, dtstart=date_1, until=date_2):
    print dt.strftime("%y-%m-%d")

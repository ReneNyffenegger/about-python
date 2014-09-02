import datetime;
import dateutil;
import dateutil.relativedelta;

date_1 = datetime.date(2010, 04, 18)
date_2 = datetime.date(2010, 06, 22)

date_diff = dateutil.relativedelta.relativedelta(date_2, date_1)

print "Diff between ", date_1, " and ", date_2, " is: " , date_diff # relativedelta(months=+2, days=+4)

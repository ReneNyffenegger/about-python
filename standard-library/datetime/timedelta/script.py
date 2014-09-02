import datetime;

today_    = datetime.date.today()
tomorrow_ = today_ + datetime.timedelta(days = 1)

print ("The date in a week will be " + tomorrow_.strftime("%Y-%m-%d"))

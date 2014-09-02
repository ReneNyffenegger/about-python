import datetime;


birthday_ = datetime.date(2014, 8, 28)
print ("Birthday: " + birthday_.strftime("%Y-%m-%d"))


# 

today_     = datetime.date.today()
in_a_week_ = today_ + datetime.timedelta(days = 7)

print ("The date in a week will be " + in_a_week_.strftime("%Y-%m-%d"))

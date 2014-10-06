import datetime

date_str = '1970-08-28 22:23:24'

dt = datetime.datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')

print (dt.strftime('%H:%M:%S %d.%m.%Y'))

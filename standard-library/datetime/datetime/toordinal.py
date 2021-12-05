import datetime

print(datetime.datetime.strptime('0001-01-01', '%Y-%m-%d').toordinal()) #      1

print(datetime.datetime.strptime('1582-10-04', '%Y-%m-%d').toordinal()) # 577725
print(datetime.datetime.strptime('1582-10-05', '%Y-%m-%d').toordinal()) # 577726 - inexisting date
print(datetime.datetime.strptime('1582-10-06', '%Y-%m-%d').toordinal()) # 577727 - inexisting date

print(datetime.datetime.strptime('1582-10-15', '%Y-%m-%d').toordinal()) # 577736 - 1st gregorian day

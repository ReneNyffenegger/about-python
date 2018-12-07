#!/usr/bin/python3
#
#      http://stackoverflow.com/a/530768/180275
#
import time

def report_time_wrong(when=time.time()):
    print (when)

report_time_wrong()   # 1544219102.503972
time.sleep(5)
                      # Note, same time again
report_time_wrong()   # 1544219102.503972


def report_time_better(when=None):
    if when is None:
       when = time.time()

    print (when)

report_time_better()  # 1544219107.5091524
time.sleep(5)
report_time_better()  # 1544219112.5136003

#
#      http://stackoverflow.com/a/530768/180275
#
import time

def report_time_wrong(when=time.time()):
    print when

report_time_wrong()   # 1406096376.71
time.sleep(5)
                      # Note, same time again
report_time_wrong()   # 1406096376.71


def report_time_better(when=None):
    if when is None:
       when = time.time()

    print when

report_time_better()  # 1406096381.71
time.sleep(5)
report_time_better()  # 1406096381.71

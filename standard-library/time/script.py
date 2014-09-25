import time

t_start = time.time()
print "Time going to sleep for four seconds."
time.sleep(4)
print "Just woke up, after {:f} seconds".format(time.time() - t_start)

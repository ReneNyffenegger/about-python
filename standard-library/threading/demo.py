import threading, time

def thread_func(name, val):

    for i in range(val):
        print(name + ": i = " + str(i))

for i in range(5):

    thread = threading.Thread(target = thread_func, args=('Thread ' + str(i), 5-i))
    thread.start()

time.sleep(1)

import time
import threading

class T(threading.Thread):

  def __init__(self, id, dur, n):

      self.id    = id
      self.dur   = dur
      self.n     = n
      super().__init__()

  def run(self):

      for i in range(self.n):
          time.sleep(self.dur) 
          print(f'{self.id}: {i} of {self.n}')
          

threads = (
    T('foo', 0.5, 5),
    T('bar', 0.6, 4),
    T('baz', 0.7, 3)
)

for t in threads:
    t.start()
      
for t in threads:
    t.join()

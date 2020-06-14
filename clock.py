#Clock unit to synchronize and parallelize work

class Clock:
  def __init__(self, time):
      self.time = time

  def currenttime(self):
    return self.time

  def clocktick(self):
      self.time = self.time+1

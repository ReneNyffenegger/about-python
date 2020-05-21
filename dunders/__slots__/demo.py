class MembersInDict:

  def __init__(self):
      self.num =  42
      self.txt = 'Hello world'

# --

class MembersInSlots:

  __slots__ = 'num', 'txt'

  def __init__(self):
      self.num =  42
      self.txt = 'Hello world'


d = MembersInDict()
s = MembersInSlots()


members_d = set(dir(d))
members_s = set(dir(s))

print(members_d - members_s)
#
#  {'__weakref__', '__dict__'}

print(members_s - members_d)
#
#  {'__slots__'}

d.dyn = 'dynamic member'

#
# Following line would throw
#    AttributeError: 'MembersInSlots' object has no attribute 'dynamic'
# if not commented.
#
# s.dynamic = 'xyz'

for k, v in d.__dict__.items():
    print(f'{k} = {v}')

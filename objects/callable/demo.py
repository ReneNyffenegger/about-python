class multiplier:

     def __init__(self, t):
         self.t = t

     def __call__(self, v):
         return self.t * v


mult_by_4 = multiplier(4)
mult_by_9 = multiplier(9)

print(mult_by_4(5)) # 20
print(mult_by_9(3)) # 27

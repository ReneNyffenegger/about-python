import sys

class CLS: pass

obj_ref_1 = CLS()

print(sys.getrefcount(obj_ref_1)) # -> 2

obj_ref_2 = obj_ref_1
obj_ref_3 = obj_ref_1

print(sys.getrefcount(obj_ref_1)) # -> 4

obj_ref_1 = CLS()

print(sys.getrefcount(obj_ref_1)) # -> 2
print(sys.getrefcount(obj_ref_2)) # -> 3

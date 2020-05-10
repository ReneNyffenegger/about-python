import ctypes

class CLS: pass

obj_ref_1 = CLS()

ob_refcnt = ctypes.c_long.from_address(id(obj_ref_1))

print(ob_refcnt.value)
#
# 1

obj_ref_2 = obj_ref_1

print(ob_refcnt.value)
#
# 2

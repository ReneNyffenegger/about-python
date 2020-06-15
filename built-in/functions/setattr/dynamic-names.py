class CLS: pass

obj = CLS()

setattr(obj, 'attr_one',  42          )
setattr(obj, 'attr_two', 'Hello world')

print(obj.attr_one, obj.attr_two)

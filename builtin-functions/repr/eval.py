#!/usr/bin/python3

var = {'foo':  42,
       'bar':'baz'
      }

var_repr = repr(var)
print('type(var_repr) = {:s}'.format(str(type(var_repr)))) # type(var_repr) = <class 'str'>

print(var_repr) # {'foo': 42, 'bar': 'baz'}
    
repr_evald = eval(var_repr)

print('type(repr_evald) = {:s}'.format(str(type(repr_evald)))) # type(repr_evald) = <class 'dict'>
                                                                  
for k,v in repr_evald.items():
    print("{:s} = {:s}".format(k, str(v)) )

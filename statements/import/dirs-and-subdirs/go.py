#
#   Store names of current local scope in global_names
#
global_names = dir()
print(global_names)
#
#  ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']

import tq84_dir

#
#  Assign list of names that are not present in global_names to new_names.
#
new_names = list(set(dir()) - set(global_names))

#
#  It turns out that importing the tq84_dir module (package) has
#  created a new name ('tq84_dir') in the current local scope.
# (global_names was created after the first call of dir() executed, hence
#  it is also reported)
#
print(new_names)
#
#  ['tq84_dir', 'global_names']

print(type(tq84_dir))
#
#  <class 'module'>

#
#  As before, store the list of attributes that are
#  present in the tq84_dir module in a variable:
#
tq84_names_init = dir(tq84_dir)

#
#  Although the directory contains two files (sub modules?), they
#  are not yet loaded:
#
print(tq84_names_init)
#
#  ['__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']

import tq84_dir.mod_one
tq84_names_1 = dir(tq84_dir)

# print(tq84_names_init)

new_names = list(set(tq84_names_1) - set(tq84_names_init))
print(new_names)
#
#  ['mod_one']


import tq84_dir.mod_two
tq84_names_2 = dir(tq84_dir)
new_names = list(set(tq84_names_2) - set(tq84_names_1))
print(new_names)
#
#  ['mod_two']

tq84_dir.mod_one.func()
#
#  I was defined in mod_one

tq84_dir.mod_two.func()
#
#  I was defined in mod_two

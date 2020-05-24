"""
  Create the following tree structure and then walk over it

   │   file.a
   │
   ├───dir-1
   │   │   file-1.b
   │   │
   │   ├───subdir-1-1
   │   │       file-1-1.c
   │   │       file-1-1.d
   │   │
   │   └───subdir-1-2
   │           file-1-2.e
   │           file-1-2.f
   │
   └───dir-2
       │   file-1.g
       │   file-1.h
       │
       ├───subdir-2-1
       │       file-2-1.i
       │
       └───subdir-2-2
               file-2-2.j
               file-2-2.k
               file-2-2.l

"""

import os
import os.path
import shutil


def createTree(under):

    curDir = os.getcwd()

    if os.path.isdir(under):
       shutil.rmtree(under)

#   os.chdir(under)

    os.mkdir(under)
    os.chdir(under)


#   for d in 'dir-1', 'dir-2':
#       if os.path.isdir(d):
#          shutil.rmtree(d)

    os.makedirs('dir-1/subdir-1-1')
    os.makedirs('dir-1/subdir-1-2')
    os.makedirs('dir-2/subdir-2-1')
    os.makedirs('dir-2/subdir-2-2')

    with open('file.a'                     , 'w'): pass

    with open('dir-1/file-1.b'             , 'w'): pass

    with open('dir-1/subdir-1-1/file-1-1.c', 'w'): pass
    with open('dir-1/subdir-1-1/file-1-1.d', 'w'): pass

    with open('dir-1/subdir-1-2/file-1-2.e', 'w'): pass
    with open('dir-1/subdir-1-2/file-1-2.f', 'w'): pass

    with open('dir-2/file-1.g'             , 'w'): pass
    with open('dir-2/file-1.h'             , 'w'): pass

    with open('dir-2/subdir-2-1/file-2-1.i', 'w'): pass

    with open('dir-2/subdir-2-2/file-2-2.j', 'w'): pass
    with open('dir-2/subdir-2-2/file-2-2.k', 'w'): pass
    with open('dir-2/subdir-2-2/file-2-2.l', 'w'): pass

    os.chdir(curDir)


def walkTree(under):

    for curDir, dirs, files in os.walk(under):
     #
     #  Note: dirs is not used here
     #

        depth = curDir.count(os.sep)

        print(f'{depth * "  "}{os.path.basename(curDir)}/')

        for file in files:
            print(f'{depth * "  "}  {file}')


testDir = 'test-dir'
createTree(testDir)
walkTree(testDir)

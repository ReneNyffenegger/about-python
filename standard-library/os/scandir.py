import os
import datetime

dir = '.' # Note: default for scandir is current directory

with os.scandir(dir) as dirEntries:
     for dirEntry in dirEntries:
         name  = dirEntry.name
       # path  = dirEntry.path
         inode = dirEntry.inode()

         stat  = dirEntry.stat()

         ctime = datetime.datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S')

         if   dirEntry.is_dir():
              type = 'dir'
         elif dirEntry.is_file():
              type = 'file'
         elif dirEntry.is_symlink():
              type = 'symlink'
         else:
              type = '?'

         print(f'{name:<25} {inode:>10} {type:<7} {ctime}')

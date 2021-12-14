import os
from typing import Mapping
import cusFun as cf
os.system('chcp 65001')

path = r"D:\共享\gcd"
mp3List = cf.find_specified_file(path=path, suffix='mp3')

key = '九幽将军'
newDir = cf.create_directory(path + '\\' + key)

for i in mp3List:

    if key in i:
        cmd = 'move' + ' '+ '"'+ i + '"'+ ' ' + newDir
        os.system(cmd)
        # print(a)

print('done')
import os,sys
import filecmp
import re
import shutil

dir1 = sys.argv[1]
dir2 = sys.argv[2]

dir1 = os.path.abspath(dir1)
dir2 = os.path.abspath(dir2)
print(dir1)
print(dir2)

print(re.sub(dir1,dir2,"/pythonstudy/module_filecmp/dir1/a"))

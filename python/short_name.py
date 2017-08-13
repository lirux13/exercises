import os
import sys
import shutil
import re

if(len(sys.argv) < 2):
    exit(-1)

pattern = sys.argv[1]
"""
print("pattern="+pattern)"""
for file in os.listdir():
    newName = file
    for i in range(1, len(sys.argv)):
        pattern = sys.argv[i]
        if pattern in file:
            fileNameRegex = re.compile(pattern)
            newName = fileNameRegex.sub('', newName)
    shutil.move(file, newName)

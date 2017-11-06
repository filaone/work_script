#!/usr/bin/python
#-*- coding:utf-8 -*-

import os
import shutil
import sys
from optparse import OptionParser
import re

def isLogFile(filename):
    pattern = re.compile(r'.*(\.){0,1}log\.\d*')
    m = pattern.match(filename)
    if m or os.path.splitext(filename)[1] == '.log':
        return True
    else:
        return False

parse = OptionParser()
parse.add_option('-s', '--src', dest="srcdir", help="please input source directory")
parse.add_option('-d', '--dest', dest="destdir", help="please input destination directory")
(option, arges) = parse.parse_args();

dest = option.destdir
src  = option.srcdir

allfile = []
for root, dirs, files in os.walk(src):
    allfile.append(root)
    for subdir in dirs:
        allfile.append(root+"/"+subdir)
    for subfile in files:
        allfile.append(root+"/"+subfile)

if not os.path.exists(dest):
    os.makedirs(dest)

for file in allfile:
    newfile = file.replace(src, dest)
    if os.path.isdir(file):
        if not os.path.exists(newfile): 
            os.makedirs(newfile)
    if os.path.isfile(file):
        if not isLogFile(file):
            shutil.copyfile(file, newfile)

print("Copy Done")

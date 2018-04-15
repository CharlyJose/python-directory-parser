from __future__ import print_function
import os
import sys
import time
import re

i=0
count=0
speed=0
if(len(sys.argv)==3):
	speed=int(sys.argv[2])

rootDir =sys.argv[1]
for dirName, subdirList, fileList in os.walk(rootDir, topdown=False):
    print('\nParsing directory: \n\t%s' % dirName)
    dir=re.split(r'/', dirName[6:])
    for i in range(0, len(dir)):     
        for j in range(0, i):
            print(' ', end='')
        print('|__', end='')
        print(" %s" % dir[i])
    time.sleep(1*speed)
    print()
    for fname in fileList:  
        for j in range(0, i):
            print(' ', end='')
        print('  -|-- %s' % fname)
    	count+=1
    if count==0:
    	print('\t(none)')
    if count!=0:
    	print('\n\t\tTotal ' + str(count) + ' files')
    count=0

#!/usr/bin/python
# -*- coding: utf-8 -*-

# sorting Kindle's My Clippings.txt file
# according to the book name
# 
# didn't check for repeatness.
# so delete the 'My Clippings.txt' file on kindle everytime!

import re
from sets import Set

f = open('My Clippings.txt','r')
MARK = u'=========='
title = f.readline()
while title:
    filename = title+'.txt'
    g = open(title,'a')
    timemark = f.readline()
    g.write(timemark)
    emptyline = f.readline()
    contentline = f.readline()
    contentlist = []
    while not re.findall(MARK,contentline):
        contentlist.append(contentline)
        contentline = f.readline()
    for line in contentlist:
        g.write(line)
    g.write(MARK)
    g.write("\n")
    title = f.readline()
f.close()
g.close()


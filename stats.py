# original author: Carter Temm https://www.github.com/cartertemm
# simple utility script to verify the existence of Lucia's license header in all files offiliated with the project
# an addition, lines and size is counted for an overall summary

header_text="""# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE."""

import fnmatch
import os
import sys
from os import stat

def recursive(directory, wildcard):
	matches = []
	for root, dirnames, filenames in os.walk(directory):
		for filename in fnmatch.filter(filenames, wildcard):
			matches.append(os.path.join(root, filename))
	return matches

def get_size(num):
	"""
	taken and modified from:
		http://code.activestate.com/recipes/578019
	"""
	symbols = ('KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
	prefix = {}
	for i, s in enumerate(symbols):
		prefix[s] = 1 << (i + 1) * 10
	for s in reversed(symbols):
		if num >= prefix[s]:
			value = float(num) / prefix[s]
			return '%.1f%s' % (value, s)
	return "%sB" % n

r=recursive("lucia", "*.py")
print("total number of .py files in this project: "+str(len(r)))
total_size=0
total_lines=0
no_header=[]
for i in r:
	f=open(i, "r")
	text=f.read()
	f.close()
	total_size+=len(text)
	total_lines+=text.count("\n")
	if not header_text in text:
		no_header.append(i)
print("total lines: "+str(total_lines))
print("total size: "+str(get_size(total_size)))
print("files without license header: "+str(len(no_header)))
if len(no_header)>0:
	print(", ".join(no_header))

# Copyright (C) 2018  LuciaSoftware and it's contributors.
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
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

"""This cli util, makes it easy to create pack files, containing a folder / subfolder structure

Just execute like lucia-cli.packer packname encryptionkey
"""

import sys
import os
from lucia.packfile import *

def progress(count, total, status=''):
	bar_len = 60
	filled_len = int(round(bar_len * count / float(total)))
	percents = round(100.0 * count / float(total), 1)
	bar = '=' * filled_len + '-' * (bar_len - filled_len)
	sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
	sys.stdout.flush()

def get_list_of_files(dirName):
	listOfFile = os.listdir(dirName)
	allFiles = list()
	# Iterate over all the entries
	for entry in listOfFile:
		# Create full path
		fullPath = os.path.join(dirName, entry)
		# If entry is a directory then get the list of files in this directory 
		if os.path.isdir(fullPath):
			allFiles = allFiles + get_list_of_files(fullPath)
		else:
			allFiles.append(fullPath)
	return allFiles

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print(f"Usage: python -m lucia-cli.packer name encryptionkey")
		sys.exit()
	
	packfilename = sys.argv[1]
	encryptionkey = sys.argv[2]
	
	print(f"Saving packfile {packfilename} in {os.getcwd()}.")
	pack = ResourceFile(encryptionkey)
	count = 0
	files_to_pack = get_list_of_files(os.getcwd())
	for entry in files_to_pack:
		pack.add_file(name=entry, internalname=entry[len(os.getcwd()):].strip("/").strip("\\\\").replace('\\', '/'))
		count = count+1
		progress(count-1, len(files_to_pack), "Packing {}".format(entry[len(os.getcwd()):].strip("/").strip("\\\\").replace('\\', '/')))
	
	print("")
	progress(len(files_to_pack)-2, len(files_to_pack), "Saving pack to disk. This may take some time. Please wait!")
	pack.save(os.path.join(os.getcwd(), packfilename))
	print("")
	progress(len(files_to_pack), len(files_to_pack), "Done")



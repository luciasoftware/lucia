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

def real_main():
	if len(sys.argv) != 3:
		print(f"Usage: lucia.packer name encryptionkey")
		sys.exit()
	
	packfilename = sys.argv[1]
	encryptionkey = sys.argv[2]
	
	pack = ResourceFile(encryptionkey)
	files_to_pack = get_list_of_files(os.getcwd())
	print("Processing files.")
	for entry in files_to_pack:
		pack.add_file(name=entry, internalname=entry[len(os.getcwd()):].strip("/").strip("\\\\").replace('\\', '/'))
	print("Done processing files.")
	print("Saving pack to disk. This can take some time. Please wait.")
	pack.save(os.path.join(os.getcwd(), packfilename))
	print(f"Done, the pack can be found in:\n{os.path.join(os.getcwd(), packfilename)}")

def clean():
	if len(sys.argv) > 1:
		sys.exit()
	
	packfilename = sys.argv[1]
	if os.path.exists(os.path.join(os.getcwd(), packfilename)):
		print("Deleting unfinished packfile.")
		os.remove(os.path.join(os.getcwd(), packfilename))
		print("Cleanup done.")

def main():
	try:
		real_main()
	except KeyboardInterrupt:
		print("Aborted by user. Cleaning up.")
		clean()


if __name__ == "__main__":
	main()

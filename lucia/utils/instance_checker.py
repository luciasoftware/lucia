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

import sys
import platform
import os
import io

if platform.system() == "Windows":
	from win32api import *
	from win32con import *
	from win32event import *
else:
	from fcntl import *


class InstanceChecker:
	"""An instance checker
	
	This is similar to bgt's instance object, to make sure a game can be running only once.
	
	args:
	    f (str): The name to be registered as a mutex.
	"""
	def __init__(self, f):
		self.running = False
		if platform.system() == "Windows":
			self.mtx = CreateMutex(None, True, f)
			if GetLastError() == 183:  # ERROR_ALREADY_EXISTS
				self.running = True
		else:
			self.fp = open(f, "w")
			try:
				lockf(self.fp, LOCK_EX | LOCK_NB)
			except IOError:
				self.running = True

	def __del__(self):
		if platform.system() == "Windows":
			CloseHandle(self.mtx)
		else:
			self.f.close()

	def is_running(self):
		"""check if another instance is already running
		
		returns:
		    True if this instance is already registered, false otherwise.
		"""
		return self.running

	def __bool__(self):
		return self.running

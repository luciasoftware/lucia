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

from configparser import *

class Configuration:
	def __init__(self):
		self.config=ConfigParser()
	
	def readInt(self, section, key):
		return self.config[section].getint(key)
	
	def readString(self, section, key):
		return str(self.config[section][key])
	
	def readFloat(self, section, key):
		return self.config[section].getfloat(key)
	
	def readBool(self, section, key):
		return self.config[section].getboolean(key)
	
	def exists(self, section):
		return self.config.has_section(section)
	
	def exists(self, section, key):
		return key in self.config[section]
	
	def writeInt(self, section, key, value):
		self.config[section][key]=int(value)
	
	def writeString(self, section, key, value):
		self.config[section][key]=str(value)
	
	def writeFloat(self, section, key, value):
		self.config[section][key]=float(value)
	
	def writeBool(self, section, key, value):
		self.config[section][key]=bool(value)
	
def loadFile(self, filename):
		with open(filename, "r") as f:
			self.read_string(f.read(), "<string>")
	
	def saveFile(self, filename):
		with open(filename, "w") as f:
			self.config.write(f)
	

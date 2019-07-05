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
#Original code by Carter Tem
import os
import math
import sound_lib
from sound_lib import stream
import lucia

class Sound(lucia.audio.Sound):
	def __init__(self):
		self.handle=None
		self.freq=44100

	def load(self,filename=""):
		if self.handle:
			self.close()
		if lucia.get_global_resource_file() is not None:
			try:
				filename = lucia.get_global_resource_file().get(filename)
			except KeyError: # the file doesn't exist in the pack file.
				if os.path.isfile(filename) == False:
					return
		if isinstance(filename, str):
			self.handle =stream.FileStream(file=filename)
		else:
			self.handle =stream.FileStream(mem=True, file=filename, length=len(filename))
		self.freq=self.handle.get_frequency()

	def play(self):
		if self.handle is None:
			return
		self.handle.looping=False
		self.handle.play()

	def play_wait(self):
		if self.handle is None:
			return
		self.handle.looping=False
		self.handle.play_blocking()

	def play_looped(self):
		if self.handle is None:
			return
		self.handle.looping=True
		self.looping=True
		self.handle.play()

	def stop(self):
		if self.handle and self.handle.is_playing:
			self.handle.stop()
			self.handle.set_position(0)

	def get_source_object(self):
		return self.handle

	def pause(self):
		if self.handle is None:
			return
		self.handle.pause()

	def resume(self):
		if self.handle is None:
			return
		self.handle.resume()

	@property
	def volume(self):
		if not self.handle:
			return False
		return float(self.handle.volume)

	@volume.setter
	def volume(self,value):
		"""Volume between 100 (full volume) to 0 silence"""
		if not self.handle:
			return False
		self.handle.set_volume(float(value/100))

	@property
	def pitch(self):
		if not self.handle:
			return False
		return (self.handle.get_frequency()/self.freq)*100

	@pitch.setter
	def pitch(self, value):
		if not self.handle:
			return False
		self.handle.set_frequency((float(value)/100)*self.freq)

	@property
	def pan(self):
		if not self.handle:
			return False
		return self.handle.get_pan()*100

	@pan.setter
	def pan(self, value):
		if not self.handle:
			return False
		self.handle.set_pan(float(value)/100)

	def close(self):
		if self.handle:
			self.handle.free()
			self.__init__()

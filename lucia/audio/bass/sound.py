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

import lucia
from sound_lib import stream

class Sound(lucia.audio.Sound):
	def __init__(self, soundfile="")):
		self.stream = None
		self.soundfile = soundfile
		if soundfile != "":
			self.load(soundfile)
	
	
	def load(self, soundfile=""):
		if soundfile == "":
			raise ValueError("No audio data provided")
		if isinstance(soundfile, str):
			self.source = stream.FileStream(mem=False, soundfile)
		if isinstance(soundfile, str):
			self.source = stream.FileStream(mem=False, soundfile)
		else:
			self.source = stream.FileStream(mem=True, io.BytesIO(soundfile)
		self.soundfile = soundfile
		return self.source
	
	def play(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.play()
		return self.source
	
	def pause(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.pause()
		return self.source
	
	def resume(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.play()
		return self.source
	
	def get_source_object(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		return self.source

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
from openal import al, alc, audio


class Sound(lucia.audio.Sound):
	def __init__(self, soundfile=""):
		self.soundfile = soundfile
		self.world = lucia.audio_backend.audio_world
		self.source = audio.SoundSource()
		if self.soundfile == "":
			return
		self.source = self.load(self.soundfile)

	def load(self, soundfile):
		if soundfile == "":
			raise ValueError("No audio data provided")
		self.soundfile = soundfile
		data = lucia.audio_backend._get_audio_data(self.soundfile)
		if data is None:
			return self.source
		self.source.queue(data)
		return self.source

	def play(self):
		self.world.play(self.source)
		self.world.update()

	def stop(self):
		try:
			self.world.stop(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def pause(self):
		try:
			self.world.pause(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def resume(self):
		try:
			self.world.resume(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def get_source_object(self):
		return self.source

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

class Sound():
	def _init__(self, soundfile=""):
		self.soundfile = soundfile
		self.loaded = False
		self.world = lucia.audio_world
		self.source = None
		if self.soundfile != "":
			self.source = self.load(self.soundfile)

		def load(self, soundfile):
			self.soundfile = soundfile
		self.source = audio.SoundSource()
		source.queue(lucia.audio._get_audio_data(soundfile))
		return source

	def play(self):
		self.world.play(source)
		self.world.update()

	def stop(self):
		try:
			self.world.stop(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def get_gain(self):
		return self.source.__getattr__(al.AL_GAIN)

	def set_gain(self, value):
		self.source.__setattr__(al.AL_GAIN, value)

	def get_pitch(self):
		return self.source.__getattr__(al.AL_PITCH)

	def set_pitch(self, value):
		self.source.__setattr__(al.AL_PITCH, value)

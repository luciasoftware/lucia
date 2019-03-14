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
	def __init__(self, soundfile=""):
		self.soundfile = soundfile
		self.world = lucia.audio_world
		self.source = audio.SoundSource()
		if self.soundfile == "":
			return
		self.source = self.load(self.soundfile)

	def load(self, soundfile):
		if soundfile == "":
			raise ValueError("No audio data provided")
		self.soundfile = soundfile
		self.source.queue(lucia.audio._get_audio_data(self.soundfile))
		return self.source

	def play(self):
		self.world.play(self.source)
		self.world.update()

	def stop(self):
		try:
			self.world.stop(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def get_gain(self):
		try:
			return self.source.__getattr__(al.AL_GAIN)
		except:
			pass

	def set_gain(self, value):
		try:
			self.source.__setattr__(al.AL_GAIN, value)
		except:
			pass

	def get_pitch(self):
		try:
			return self.source.__getattr__(al.AL_PITCH)
		except:
			pass

	def set_pitch(self, value):
		try:
			self.source.__setattr__(al.AL_PITCH, value)
		except:
			pass

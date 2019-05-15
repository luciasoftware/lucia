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
from sound_lib import listener, main, music, input, output, stream

class SoundPool(lucia.audio.SoundPool):
	def __init__(self, *args):
		self.listener = listener.Listener()
		self.sources = []

	def play_stationary(self, soundfile):
		source = None
		if soundfile == "":
			raise ValueError("No audio data provided")
		if isinstance(soundfile, str):
			source = stream.FileStream(mem=False, file=soundfile)
		else:
			source = stream.FileStream(mem=True, file=io.BytesIO(soundfile))
		source.play()
		self.sources.append(source)
		return source

	def play_1d(self, soundfile, x):
		return self.play3d(soundfile, x, 0, 0)

	def play_2d(self, soundfile, x, y):
		return self.play3d(soundfile, x, y, 0)

	def play_3d(self, soundfile, x, y, z):
		source = None
		if soundfile == "":
			raise ValueError("No audio data provided")
		if isinstance(soundfile, str):
				source = stream.FileStream(mem=False, file=soundfile)
		else:
			source = stream.FileStream(mem=True, file=io.BytesIO(soundfile))
		source.set_3d_position(position=(x,y,z))
		source.play()
		self.sources.append(source)
		return source

	def update_listener1d(self, x):
		self.update_listener3d(x,0,0)

	def update_listener2d(self, x,y):
		self.update_listener3d(x,y,0)

	def update_listener3d(self, x,y,z):
		self.listener.set_3d_position(position=(x,y,z))

	def update_audio_system(self):
		pass

	def get_source_object(self):
		raise NotImplementedError

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

from openal import *
from math import pi, cos, sin, radians
import io

class SoundPool():
	def __init__(self, rolloff_factor = 0.5, max_distance=10):
		self.sources = []
		self.listener = oalGetListener()
		self.rolloff_factor = rolloff_factor
		self.all_paused = False
		self.max_distance = max_distance

	def __del__(self):
		for source in self.sources:
			source.stop()

	def set_rolloff_factor(self, value):
		self.rolloff_factor = value

	def set_max_distance(self, max_distance):
		self.max_distance = max_distance

	def pause_all(self):
		for source in self.sources:
			source.pause()
		self.all_paused = True

	def resume_all(self):
		for source in self.sources:
			source.play()
		self.all_paused = False

	def play_stationary(self, soundfile, looping = False):
		if isinstance(soundfile, str):
			source = oalOpen(soundfile)
		else:
			f = WaveFile(io.BytesIO(soundfile))
			b = Buffer(f)
			source = Source(b)
		source.set_looping(looping)
		source.play()
		self.sources.append(source)
		return source

	def play_1d(self, soundfile, x, looping = False, rolloff_factor = -1):
		if isinstance(soundfile, str):
			source = oalOpen(soundfile)
		else:
			f = WaveFile(io.BytesIO(soundfile))
			b = Buffer(f)
			source = Source(b)
		source.set_position((x,0,0))
		source.set_looping(looping)
		source.set_rolloff_factor(self.rolloff_factor)
		source.set_max_distance(self.max_distance)
		source.play()
		self.sources.append(source)
		return source

	def play_2d(self, soundfile, x, y, looping = False, rolloff_factor = -1):
		if isinstance(soundfile, str):
			source = oalOpen(soundfile)
		else:
			f = WaveFile(io.BytesIO(soundfile))
			b = Buffer(f)
			source = Source(b)
		source.set_position((x,0,-y))
		source.set_looping(looping)
		source.set_rolloff_factor(self.rolloff_factor)
		source.set_max_distance(self.max_distance)
		source.play()
		self.sources.append(source)
		return source

	def play_3d(self, soundfile, x, y, z, looping = False):
		if isinstance(soundfile, str):
			source = oalOpen(soundfile)
		else:
			f = WaveFile(io.BytesIO(soundfile))
			b = Buffer(f)
			source = Source(b)
		source.set_position((x,z,-y))
		source.set_looping(looping)
		source.set_rolloff_factor(self.rolloff_factor)
		#source.set_max_distance(self.max_distance)
		source.play()
		self.sources.append(source)
		return source

	def update_listener_1d(self, x):
		self.listener.move_to((x,0,0))

	def update_listener_2d(self, x, y):
		self.listener.move_to((x,0,-y))

	def update_listener_3d(self, x, y, z, direction=0, zdirection=0):
		if direction > 360:
			direction = direction - 360
		self.listener.set_position((x,z,-y))
		ox=0+cos(radians(direction))
		oy=0+sin(radians(direction))
		oz=0+sin(radians(zdirection))
		self.listener.set_orientation((ox, oz, -oy, 0, 1, 0))

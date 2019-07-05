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
from math import pi, cos, sin, radians
from .loaders import *
import io


class SoundPool(lucia.audio.SoundPool):
	def __init__(self, rolloff_factor=0.5, max_distance=10):
		self.sources = []
		self.all_paused = False
		self.default_rolloff_factor = rolloff_factor
		self.world = lucia.get_audio_backend().audio_world
		self.listener = self.world.listener
		# get list of available htrf tables
		self.hrtf_buffers = [alc.ALCint(), alc.ALCint * 4, alc.ALCint()]
		alc.alcGetIntegerv(
			self.world.device, alc.ALC_NUM_HRTF_SPECIFIERS_SOFT, 1, self.hrtf_buffers[0]
		)
		# attributes for device to set specified hrtf table
		self.hrtf_select = self.hrtf_buffers[1](
			alc.ALC_HRTF_SOFT, alc.ALC_TRUE, alc.ALC_HRTF_ID_SOFT, 1
		)
		lucia.get_audio_backend().sound_pools.append(self)

	def set_hrtf(self, num):
		if num == None:
			alc.alcResetDeviceSOFT(self.world.device, None)
		elif num >= 0 and num <= self.hrtf_buffers[0].value:
			self.hrtf_select[3] = num
			# reset the device so the new hrtf settings take effect
			alc.alcResetDeviceSOFT(self.world.device, self.hrtf_select)

	# confirm hrtf has been loaded and is enabled
	def is_hrtf_enabled(self):
		alc.alcGetIntegerv(self.world.device, alc.ALC_HRTF_SOFT, 1, self.hrtf_buffers[2])
		if self.hrtf_buffers[2].value == alc.ALC_HRTF_DISABLED_SOFT:
			return False
		elif self.hrtf_buffers[2].value == alc.ALC_HRTF_ENABLED_SOFT:
			return True
		elif self.hrtf_buffers[2].value == alc.ALC_HRTF_DENIED_SOFT:
			return False
		elif self.hrtf_buffers[2].value == alc.ALC_HRTF_REQUIRED_SOFT:
			return True
		elif self.hrtf_buffers[2].value == alc.ALC_HRTF_HEADPHONES_DETECTED_SOFT:
			return True
		elif self.hrtf_buffers[2].value == alc.ALC_HRTF_UNSUPPORTED_FORMAT_SOFT:
			return False

	def __del__(self):
		del lucia.get_audio_backend().sound_pools[self]

	def pause_all(self):
		for source in self.sources:
			self.world.pause(source)
		self.world.update()
		self.all_paused = True

	def resume_all(self):
		for source in self.sources:
			self.world.play(source)
		self.world.update()
		self.all_paused = False

	def stop(self, source):
		try:
			self.world.stop(source)
		except:
			raise lucia.audio.SoundNotPlayingError(f"Sound {source} is no longer playing.")

	def play_stationary(self, soundfile, looping=False):
		source = audio.SoundSource()
		data = lucia.audio_backend._get_audio_data(soundfile)
		if data is None:
			return source
		source.queue(data)
		self.world.play(source)
		self.world.update()
		self.sources.append(source)
		return source

	def play_1d(self, soundfile, x, looping=False, rolloff_factor=-1):
		return self.play_3d(soundfile, x, 0, 0, looping, rolloff_factor)

	def play_2d(self, soundfile, x, y, looping=False, rolloff_factor=-1):
		return self.play_3d(soundfile, x, y, 0, looping, rolloff_factor)

	def play_3d(
		self, soundfile, x, y, z, looping=False, pitch=1.0, volume=1.0, rolloff_factor=0.5
	):
		source = audio.SoundSource(1.0, pitch, (x, z, -y))
		data = lucia.audio_backend._get_audio_data(soundfile)
		if data is None:
			return source
		source.queue(data)
		source.looping = looping
		self.world.play(source)
		self.world.update()
		self.sources.append(source)
		return source

	def update_sound_position(self, source, x, y, z):
		source.position = (x, z, -y)

	def update_listener1d(self, x):
		self.update_listener_3d(x, 0, 0)

	def update_listener2d(self, x, y):
		self.update_listener_3d(x, y, 0)

	def update_listener3d(self, x, y, z, direction=90, zdirection=0):
		if direction > 360:
			direction = direction - 360
		self.listener.position = (x, z, -y)
		ox = 0 + cos(radians(direction))
		oy = 0 + sin(radians(direction))
		oz = 0 + sin(radians(zdirection))
		self.listener.orientation = (ox, oz, -oy, 0, 1, 0)
		self.world.update()

	def update_audio_system(self):
		self.world.update()

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
from openal import (
	audio as oAudio,
)  # if not done this way, it will conflict will lucia.audio
from .soundpool import *
from .sound import *

audio_world = None
sound_pools = []


class OpenALAudioBackend(lucia.audio.AudioBackend):
	# this function most be called for each wrapper.
	def initialize(self):
		global audio_world
		audio_world = oAudio.SoundSink()
		audio_world.activate()

	def quit(self):
		pass  # nothing needed here.

	# This function most be called for each wrapper.
	def update_audio_system(self):
		audio_world.update()

	def is_hrtf_compatible(self):
		return False

	def enable_hrtf(self, should_enable):
		raise lucia.audio.BackActionNotSupported(
			"ENabling HRTF back wide is not available with the OpenAL backend"
		)


# below is all the wrapper specific stuff.
class SoundNotPlayingError(ValueError):
	pass


class UnsupportedAudioFormatError(Exception):
	pass


def _get_audio_data(filename):
	if lucia.get_global_resource_file() is not None:
		try:
			filename = lucia.get_global_resource_file().get(filename)
		except KeyError:
			if os.path.isfile(filename) == False:
				return None
	if isinstance(filename, str):
		data = load_file(filename)
	else:
		try:
			data = load_wav_file(io.BytesIO(filename))
		except wave.Error:
			data = load_ogg_file(io.BytesIO(filename))
		except:
			raise UnsupportedAudioFormatError()
	return data

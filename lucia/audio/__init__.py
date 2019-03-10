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

from .soundpool import *
from .sound import *

class SoundNotPlayingError(ValueError):
	pass

class UnsupportedAudioFormatError(Exception):
	pass

def _get_audio_data(soundfile):
	if isinstance(soundfile, str):
		data = load_file(soundfile)
	else:
		try:
			data = load_wav_file(io.BytesIO(soundfile))
		except wave.Error:
			data = load_ogg_file(io.BytesIO(soundfile))
		except:
			raise UnsupportedAudioFormatError()
	return data


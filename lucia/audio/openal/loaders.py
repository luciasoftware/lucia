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

"""Utility functions for loading sounds."""
import os
import sys
import wave
import io
import soundfile as sf
from openal.audio import SoundData


def load_ogg_file(fname):
	"""Loads a ogg encoded audio file converts it to wav and returns a SoundData object."""
	finish = io.BytesIO(b"")
	with sf.SoundFile(fname, "rb") as start:
		data = start.read()
		out = sf.SoundFile(
			finish,
			"wb",
			samplerate=start.samplerate,
			channels=start.channels,
			format="wav",
			subtype="PCM_16",
		)
		out.write(data)
		start.close()
		out.close()
		finish.seek(0)
		return load_wav_file_mem(finish.read())


def load_wav_file(fname):
	"""Loads a WAV encoded audio file into a SoundData object."""
	fp = wave.open(fname, "rb")
	channels = fp.getnchannels()
	bitrate = fp.getsampwidth() * 8
	samplerate = fp.getframerate()
	buf = fp.readframes(fp.getnframes())
	return SoundData(buf, channels, bitrate, len(buf), samplerate)


def load_wav_file_mem(data):
	"""Loads WAV encoded audio data into a SoundData object."""
	fp = wave.open(io.BytesIO(data), "rb")
	channels = fp.getnchannels()
	bitrate = fp.getsampwidth() * 8
	samplerate = fp.getframerate()
	buf = fp.readframes(fp.getnframes())
	return SoundData(buf, channels, bitrate, len(buf), samplerate)


# supported extensions
_FILEEXTENSIONS = {".wav": load_wav_file, ".ogg": load_ogg_file}


def load_file(fname):
	"""Loads an audio file into a SoundData object."""
	ext = os.path.splitext(fname)[1].lower()
	funcptr = _FILEEXTENSIONS.get(ext, None)
	if not funcptr:
		raise ValueError("unsupported audio file type")
	return funcptr(fname)

"""Utility functions for loading sounds."""
import os
import sys
import wave
import io
from openal.audio import SoundData

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
_FILEEXTENSIONS = {".wav": load_wav_file}


def load_file(fname):
    """Loads an audio file into a SoundData object."""
    ext = os.path.splitext(fname)[1].lower()
    funcptr = _FILEEXTENSIONS.get(ext, None)
    if not funcptr:
        raise ValueError("unsupported audio file type")
    return funcptr(fname)

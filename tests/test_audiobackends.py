import os

from . import util

import lucia

audio_file_path = os.path.join(os.getcwd(), "tests", "audio.ogg")

def test_bass():
	lucia.initialize(audiobackend=lucia.AudioBackend.BASS)
	assert lucia.running == True
	
	testsound = lucia.audio_backend.Sound()
	testsound.load(audio_file_path)
	testsound.play()
	assert testsound.get_source_object().is_playing
	testpool = lucia.audio_backend.SoundPool()
	testpool.play_stationary(audio_file_path)
	testpool.play1d(audio_file_path)
	testpool.play2d(audio_file_path)
	testpool.play3d("audio.ogg")
	testpool.update_audio_system()
	testpool.update_listener1d(1)
	testpool.update_listener2d(1,2)
	testpool.update_listener3d(1,2,3)

import os

from . import util

import lucia

audio_file_path = os.path.join(os.getcwd(), "tests", "audio.ogg")


def test_bass():
	lucia.initialize(audiobackend=lucia.AudioBackend.BASS)
	assert lucia.running == True
	
	print(f"Playing sound {audio_file_path}.")
	testsound = lucia.audio_backend.Sound()
	testsound.load(audio_file_path)
	testsound.play()
	assert testsound.get_source_object().is_playing
	testpool = lucia.audio_backend.SoundPool()
	testpool.play_stationary(audio_file_path)
	testpool.play_1d(audio_file_path, 0, 1000, False)
	testpool.play_2d(audio_file_path, 0, 0, 1000, 1000, False)
	testpool.play_3d(audio_file_path, 0, 0, 0, 1000, 1000, 1000, False)
	testpool.update_audio_system()
	testpool.update_listener_1d(1)
	testpool.update_listener_2d(1, 2)
	testpool.update_listener_3d(1, 2, 3, 0)

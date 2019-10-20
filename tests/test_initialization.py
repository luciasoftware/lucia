# test startup of lucia
from . import util

import pytest
import lucia


@pytest.mark.skip()
def test_initialization_openal():
	lucia.initialize(audiobackend=lucia.AudioBackend.OPENAL)
	assert lucia.running == True

@pytest.mark.skip()
def test_audio_backend_initialization():
	if lucia.running == False:
		lucia.initialize()
	assert lucia.audio_backend is not None
	assert lucia.audio_backend_class is not None


@pytest.mark.skip()
def test_show_window():
	if lucia.running == False:
		lucia.initialize()
	lucia.show_window()
	assert lucia.window is not None


@pytest.mark.skip()
def test_process_events():
	if lucia.running == False:
		lucia.initialize()
	assert lucia.process_events() is not None

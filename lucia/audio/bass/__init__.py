import lucia
from .sound import *
from .soundpool import *

from sound_lib import listener, main, music, input, output, stream

generic_output = None # used for sounds objects.

class BassAudioBackend(lucia.audio.AudioBackend):
	def initialize(self):
		global generic_output
		
	
	def quit(self):
		pass
	
	def is_hrtf_compatible(self):
		return False
	
	def enable_hrtf(self, should_enable):
		raise lucia.audio.BackActionNotSupported("ENabling HRTF back wide is not available with the OpenAL backend")
	
	def update_audio_system(self):
		raise lucia.AudioBackendException("BASS wrapper not implemented yet.")

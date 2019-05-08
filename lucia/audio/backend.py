from abc import ABC, abstractmethod

class AudioBackend(ABC):
	@abstractmethod
	def initialize(self):
		pass
	
	@abstractmethod
	def update_audio_system(self):
		pass
	
	@abstractmethod
	def quit(self):
		pass
	
	@abstractmethod
	def is_hrtf_compatible(self):
		pass
	
	@abstractmethod
	def enable_hrtf(self, should_enable):
		pass

class BackActionNotSupported(ValueError):
	pass

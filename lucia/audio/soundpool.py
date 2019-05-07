from abc import ABC, abstractmethod

class SoundPool(ABC):
	@abstractmethod
	def play_stationary(*args, **kwargs):
		pass
	def play3d(*args, **kwargs):
		pass
	
	@abstractmethod
	def update_listener3d(*args, **kwargs):
		pass
	
	@abstractmethod
	def update_audio_system(*args, **kwargs):
		pass
	
	@abstractmethod
	def get_source_object(*args, **kwargs):
		pass

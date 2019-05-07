"""Base class for the soundpool. All audio backends sound pool classes will inheriate from this class"""

from abc import ABC, abstractmethod

class SoundPool(ABC):
	@abstractmethod
	def __init__(self, *args, **kwargs):
		pass
		
	@abstractmethod
	def play3d(self, *args, **kwargs):
		pass
		
	@abstractmethod
	def update_listener3d(self, *args, **kwargs):
		pass
		
	@abstractmethod
	def update_audio_system(self, *args, **kwargs):
		pass

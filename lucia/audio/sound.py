from abc import ABC, abstractmethod

class Sound(ABC):
	@abstractmethod
	def load(*args, **kwargs):
		pass
	
	@abstractmethod
	def play(*args, **kwargs):
		pass
	
	@abstractmethod
	def pause(*args, **kwargs):
		pass
	
	@abstractmethod
	def resume(*args, **kwargs):
		pass
	
	@abstractmethod
	def get_source_object(*args, **kwargs):
		pass


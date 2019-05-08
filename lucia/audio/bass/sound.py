import lucia
from sound_lib import stream

class Sound(lucia.audio.Sound):
	def __init__(self, soundfile="")):
		self.stream = None
		self.soundfile = soundfile
		if soundfile != "":
			self.load(soundfile)
	
	
	def load(self, soundfile=""):
		if soundfile == "":
			raise ValueError("No audio data provided")
		if isinstance(soundfile, str):
			self.source = stream.FileStream(mem=False, soundfile)
		if isinstance(soundfile, str):
			self.source = stream.FileStream(mem=False, soundfile)
		else:
			self.source = stream.FileStream(mem=True, io.BytesIO(soundfile)
		self.soundfile = soundfile
		return self.source
	
	def play(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.play()
		return self.source
	
	def pause(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.pause()
		return self.source
	
	def resume(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		self.source.play()
		return self.source
	
	def get_source_object(self):
		if self.source is None:
			raise ValueError("Sound data not loaded.")
		return self.source

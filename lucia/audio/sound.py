import io, pygame
from openal import *

class Sound():
	def __init__(self):
		self.initialized = False
		self.source = Source()

	def __del__(self):
		try:
			self.source.stop()
		except:
			pass

	def load(self, soundfile="", looping=False):
		if soundfile == "":
			print("empty")
			return
		if isinstance(soundfile, str):
			print("str")
			source = oalOpen(soundfile)
		else:
			print("bytes")
			f = WaveFile(io.BytesIO(soundfile))
			b = Buffer(f)
			self.source = Source(b)
		self.source.set_looping(looping)
		self.initialized = True

	def get_source(self):
		return self.source

	def set_volume(self, v):
		self.source.set_gain((v/100))

	def play(self):
		if self.initialized == False:
			return
		if self.isPlaying():
			return
		self.source.play()
		self.running = True

	def play_wait(self):
		self.source.play()
		while self.source.get_state() == AL_PLAYING:
			pygame.event.poll()

	def stop(self):
		if self.isPlaying():
			self.source.stop()
			self.running = False

	def pause(self):
		self.source.pause()

	def is_playing(self):
		return self.source.get_state() == AL_PLAYING


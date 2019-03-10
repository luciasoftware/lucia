import lucia
from openal import al, alc, audio

class Sound():
	def _init__(self, soundfile=""):
		self.soundfile = soundfile
		self.loaded = False
		self.world = lucia.audio_world
		self.source = None
		if self.soundfile != "":
			self.source = self.load(self.soundfile)

		def load(self, soundfile):
			self.soundfile = soundfile
		self.source = audio.SoundSource()
		source.queue(lucia.audio._get_audio_data(soundfile))
		return source

	def play(self):
		self.world.play(source)
		self.world.update()

	def stop(self):
		try:
			self.world.stop(self.source)
		except:
			raise SoundNotPlayingError(f"Sound {source} is no longer playing.")


import lucia
from sound_lib import listener, main, music, input, output, stream

class SoundPool(lucia.audio.SoundPool):
	def __init__(self, *args):
		self.output = output.ThreeDOutput(args)
		self.output.start()
		self.listener = listener.Listener()
		self.sources = []

	def play_stationary(self, soundfile):
		source = None
		if soundfile == "":
			raise ValueError("No audio data provided")
		if isinstance(soundfile, str):
			source = stream.FileStream(mem=False, soundfile)
		if isinstance(soundfile, str):
			source = stream.FileStream(mem=False, soundfile)
		else:
			source = stream.FileStream(mem=True, io.BytesIO(soundfile)
		source.play()
		self.sources.append(source)
		return source

import sdl2
import lucia

class VirtualInput():
	def __init__(self, message, password=False):
		self.text = ""
		self.message = message
		self.password = password

	def run(self):
		while True:
			events = lucia.process_events()
			for event in events:
				if event.type == sdl2.SDL_KEYDOWN:
					if event.key.keysym.sym in (sdl2.SDLK_DOWN, sdl2.SDLK_UP):
						lucia.output.output(self.text)
					# some way of detecting a-z A-Z and 0-9 here.

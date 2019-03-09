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
						continue
					if event.key.keysym.sym == sdl2.SDLK_BACKSPACE:
						if len(self.text) == 0:
							continue
						last = self.text[-1]
						self.text = self.text[:-1]
						lucia.output.output(last + " deleted") if self.password == False else lucia.output.output("hidden deleted")
					if event.key.keysym.sym == sdl2.SDLK_RETURN:
						return self.text
					if event.key.keysym.sym == sdl2.SDLK_SPACE:
						self.text += " "
						lucia.output.output("space") if self.password == False else lucia.output.output("hidden")
					try:
						if chr(event.key.keysym.sym).isalnum():
							self.text += chr(event.key.keysym.sym)
							lucia.output.output(chr(event.key.keysym.sym)) if self.password == False else lucia.output.output("hidden")
					except ValueError:
						continue

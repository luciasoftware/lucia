import lucia
import sdl2
import time

class Menu():
	def __init__(self, scroll_sound="", enter_sound="", open_sound="", border_sound="", music=""):
		self.running = False
		self.items = {}
		self.shouldInterrupt = True
		self.pool = lucia.audio.SoundPool()
		self.enter_sound = enter_sound
		self.scroll_sound = scroll_sound
		self.open_sound = open_sound
		self.border_sound = border_sound
		self.music = music
		self.add_speech_method(lucia.output)

	def add_speech_method(self, method, shouldInterrupt=True):
		self.speechMethod = method
		self.shouldInterrupt = shouldInterrupt

	def add_item_tts(self, item, internal_name=""):
		if internal_name == "":
			self.items[item] = item
		else:
			self.items[item] = internal_name

	def run(self, intro="", interrupt=True):
		music = ""
		self.count = 0
		self.running = True
		if self.music:
			music = self.pool.play_stationary(self.music, True)
			music.__setattr__("gain", 0.5)
		if self.open_sound != "":
			self.pool.play_stationary(self.open_sound)
		if intro != "":
			self.speechMethod.speak(intro, interrupt)
		while self.running and lucia.running:
			lucia.process_events()
			time.sleep(0.005)
			if lucia.key_pressed(sdl2.SDLK_ESCAPE):
				if self.enter_sound != "":
					self.pool.play_stationary(self.enter_sound)
					self.pool.stop(music)
				return "-1"
			if lucia.key_pressed(sdl2.SDLK_DOWN):
				if self.count < len(self.items)-1:
					self.count = self.count+1
					if self.scroll_sound != "":
						self.pool.play_stationary(self.scroll_sound)
				else:
					if self.border_sound != "":
						self.pool.play_stationary(self.border_sound)
				self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
			if lucia.key_pressed(sdl2.SDLK_UP):
				if self.count > 0:
					self.count = self.count-1
					if self.scroll_sound != "":
						self.pool.play_stationary(self.scroll_sound)
				else:
					if self.border_sound != "":
						self.pool.play_stationary(self.border_sound)
				self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
			if lucia.key_pressed(sdl2.SDLK_RETURN):
				if self.enter_sound != "":
					self.pool.play_stationary(self.enter_sound)
				self.running = False
				self.pool.stop(music)
		return self.items[list(self.items)[self.count]]

class YesNoMenu(Menu):
	def __init__(scroll_sound="", enter_sound="", open_sound="", border_sound=""):
		Menu.__init__(scroll_sound, enter_sound, open_sound, border_sound)
		self.add_item_tts("Yes", "yes")
		self.add_item_tts("No", "No")

# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

import lucia
import sdl2
import time

class Menu():
	def __init__(self, scroll_sound="", enter_sound="", open_sound="", border_sound="", music=""):
		self.running = False
		self.items = {}
		self.shouldInterrupt = True
		self.enter_sound = lucia.audio.Sound()
		self.scroll_sound = lucia.audio.Sound()
		self.open_sound = lucia.audio.Sound()
		self.border_sound = lucia.audio.Sound()
		self.music = lucia.audio.Sound()
		# in this example we catch the exceptions to allow the end developer to provide no sounds without problems.
		try:
			self.enter_sound.load(enter_sound)
		except ValueError:
			pass
		try:
			self.scroll_sound .load(scroll_sound)
		except ValueError:
			pass
		try:
			self.open_sound.load(open_sound)
		except ValueError:
			pass
		try:
			self.border_sound.load(border_sound)
		except ValueError:
			pass
		try:
			self.music.load(music)
		except ValueError:
			pass
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
		self.count = 0
		self.running = True
		if self.music:
			self.music.play()
			self.music.set_gain(0.3)
		if self.open_sound != "":
			self.open_sound.play()
		if intro != "":
			self.speechMethod.speak(intro, interrupt)
		while self.running and lucia.running:
			lucia.process_events()
			time.sleep(0.005)
			if lucia.key_pressed(sdl2.SDLK_ESCAPE):
				if self.enter_sound != "":
					self.enter_sound.play()
					try:
						self.music.stop()
					except: # thrown if no music was specified.
						pass
				return "-1"
			if lucia.key_pressed(sdl2.SDLK_DOWN):
				if self.count < len(self.items)-1:
					self.count = self.count+1
					if self.scroll_sound != "":
						self.scroll_sound.play()
				else:
					if self.border_sound != "":
						self.border_sound.play()
				self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
			if lucia.key_pressed(sdl2.SDLK_UP):
				if self.count > 0:
					self.count = self.count-1
					if self.scroll_sound != "":
						self.scroll_sound.play()
				else:
					if self.border_sound != "":
						self.border_sound.play()
				self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
			if lucia.key_pressed(sdl2.SDLK_RETURN):
				if self.enter_sound != "":
					self.enter_sound.play()
				self.running = False
				try:
					self.music.stop()
				except: # thrown if no music was selected
					pass
		return self.items[list(self.items)[self.count]]

class YesNoMenu(Menu):
	def __init__(*args):
		Menu.__init__(args)
		self.add_item_tts("Yes", "yes")
		self.add_item_tts("No", "No")

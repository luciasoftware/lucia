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

from ..audio.soundpool import *
import time, pygame

class Menu():
	def __init__(self, scroll_sound="", enter_sound="", open_sound="", border_sound=""):
		self.running = False
		self.items = {}
		self.shouldInterrupt = True
		self.pool = SoundPool()
		self.enter_sound = enter_sound
		self.scroll_sound = scroll_sound
		self.open_sound = open_sound
		self.border_sound = border_sound

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
		if self.open_sound != "":
			self.pool.play_stationary(self.open_sound)
		if intro != "":
			self.speechMethod.speak(intro, interrupt)
		while self.running:
			time.sleep(0.005)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						if self.enter_sound != "":
							self.pool.play_stationary(self.enter_sound)
						return "-1"
					if event.key == pygame.K_DOWN:
						if self.count < len(self.items)-1:
							self.count = self.count+1
							if self.scroll_sound != "":
								self.pool.play_stationary(self.scroll_sound)
						else:
							if self.border_sound != "":
								self.pool.play_stationary(self.border_sound)
						self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
					if event.key == pygame.K_UP:
						if self.count > 0:
							self.count = self.count-1
							if self.scroll_sound != "":
								self.pool.play_stationary(self.scroll_sound)
						else:
							if self.border_sound != "":
								self.pool.play_stationary(self.border_sound)
						self.speechMethod.speak(list(self.items)[self.count], self.shouldInterrupt)
					if event.key == pygame.K_RETURN:
						if self.enter_sound != "":
							self.pool.play_stationary(self.enter_sound)
						self.running = False
		return self.items[list(self.items)[self.count]]

class YesNoMenu(Menu):
	def __init__(scroll_sound="", enter_sound="", open_sound="", border_sound=""):
		Menu.__init__(scroll_sound, enter_sound, open_sound, border_sound)
		self.add_item_tts("Yes", "yes")
		self.add_item_tts("No", "No")

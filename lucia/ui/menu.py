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
		"""audiogame virtual menu
		
		This object functions as an audiogame menu, where up/down/enter can be used to interact and choose an option.
		Sounds such as the movement sound, selection sound, etc may be specified.
		This is an almost direct conversion of bgt's dynamic_menu class, though it contains some enhancements found in other extensions such as m_pro.
		
		args:
		    :param scroll_sound (str, optional): File name of the sound that will be played when the cursor moves within the menu because an arrow key was pressed.
		    :param enter_sound (str, optional): File name of the sound that will be played when enter is pressed to choose an option.
		    :param open_sound (str, optional): File name of the sound that will be played when the menu is presented to the user.
		    :param border_sound (str, optional): File name of the sound played when you hit the edge of the menu when trying to move.
		    :param music (str, optional): File name of the background music that will be played while this menu is running.
		"""
		self.running = False
		self.items = {}
		self.shouldInterrupt = True
		self.enter_sound = lucia.audio_backend.Sound()
		self.scroll_sound = lucia.audio_backend.Sound()
		self.open_sound = lucia.audio_backend.Sound()
		self.border_sound = lucia.audio_backend.Sound()
		self.music = lucia.audio_backend.Sound()
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
		"""selects the speech method and interrupt flag
		
		args:
		    :param method (obj): The method to use. This method should be either a module or a class and provide the necessary output functions, see lucia.output for an example.
		    :param shouldInterrupt (bool, optional): determines if this speech method should interrupt already existing speech when speaking something new. Default is True.
		"""
		self.speechMethod = method
		self.shouldInterrupt = shouldInterrupt

	def add_item_tts(self, item, internal_name=""):
		"""adds a spoken item to the menu.
		
		args:
		    :param item (str): The text of the item to be added. This is the text you will here when you come across it in the menu.
		    :param internal_name (str, optional): The internal name of this item. when you retrieve the selected item by name this will be returned. Defaults to the spoken text of the item.
		"""
		if internal_name == "":
			self.items[item] = item
		else:
			self.items[item] = internal_name

	def run(self, intro="select an option", interrupt=True):
		"""presents this menu to the user.
		
		This function blocks until the menu is closed, either by selecting an item or pressing escape.
		Available controls are up/down arrows, enter, and escape. Wrapping is not supported.
		
		args:
		    :param intro (str, optional): The text that will be spoken when the menu is presented, this will occur at the same time as the open sound. Default is 'select an option'
		    :param interrupt (bool, optional): Determines if speech is interrupted when it is queued to be spoken. For your sanity, this should always be True. Defaults to True.
		
		returns:
		str if an option was selected, containing the option's internal name. -1 if escape was pressed.
		"""
		self.count = 0
		self.running = True
		if self.music:
			self.music.play()
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
		"""A yes/no menu
		
		This simply takes a menu and initializes it with options of Yes and No, you would then have to call run and get the return.
		The internal names of the items are lower case.
		
		args:
		    :param args (tuple): Set of arguments to pass to menu.__init__
		"""
		Menu.__init__(args)
		self.add_item_tts("Yes", "yes")
		self.add_item_tts("No", "No")

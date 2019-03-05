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

import os, pygame, time, platform
from ..speechcontroller import SpeechController
from ..resourcemanager import ResourceManager
from .menu import Menu
from .. import globals
from ..steel.ScreenReader import ScreenReader

# This is a wrapper around lucia/speechcontroller.py, that provides a male and a female voice along with screen reader output.
class SpeechSystem():
	def __init__(self, password):
		self.male = SpeechController()
		self.female = SpeechController()
		self.sr = ScreenReader()
		self.password = password
		self.default_rate=-1
		if platform.system() == "Windows":
			self.default_rate = 0
		else:
			self.default_rate = 250

	def first_time_configuration(self):
		if os.path.isfile(os.path.join(globals.data_dir, "voicedata.dat")) == False:
			self.setup()
			return
		else:
			voiceData = ResourceManager()
			voiceData.load_resources(os.path.join(globals.data_dir, "voicedata.dat"), self.password)
			self.male = SpeechController()
			self.male.set_voice(voiceData.get("male.voice").decode())
			self.male.rate(int(voiceData.get("male.rate").decode()))
			self.female = SpeechController()
			self.female.set_voice(voiceData.get("female.voice").decode())
			self.female.rate(int(voiceData.get("female.rate").decode()))

	def setup(self):
		self.sr.speak("Setup voices for the game")
		self.sr.speak("You can change this at any time from the main menu.")
		# male
		mv = self.voiceSelector(self.male, "Select the male voice you want to use.")
		self.male.set_voice(mv)
		mr = self.rateSelector(self.male, "Select the rate for the male voice. Press the spacebar to hear a test sentence with the selected voice and rate.")
		self.male.rate(mr)
		# female
		fv = self.voiceSelector(self.female, "Select the female voice you want to use.")
		self.female.set_voice(fv)
		fr = self.rateSelector(self.female, "Select the rate for the female voice. Press the spacebar to hear a test sentence with the selected voice and rate.")
		self.female.rate(fr)
		# save.
		voiceData = ResourceManager()
		voiceData.set("male.voice", mv.encode())
		voiceData.set("male.rate", str(mr).encode())
		voiceData.set("female.voice", fv.encode())
		voiceData.set("female.rate", str(fr).encode())
		voiceData.save_resources(os.path.join(globals.data_dir, "voicedata.dat"), self.password)

	def get_male_voice(self):
		return self.male

	def get_female_voice(self):
		return self.female

	def get_screen_reader(self):
		return self.sr


	# internal functions.
	def voiceSelector(self, engine, intro):
		self.sr.speak(intro)
		if engine!=None and self.default_rate!=None:
			engine.rate(self.default_rate)
		import platform
		items = []
		for voice in engine.get_available_voices():
			if platform.system().lower() == "darwin":
				items.append(voice[33:])
			else:
				items.append(voice)
		count = 0
		running = True
		while running:
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_DOWN:
						if count < len(items)-1:
							count = count+1
						if platform.system().lower() == "darwin":
							engine.voice("com.apple.speech.synthesis.voice."+list(items)[count])
						else:
							engine.voice(list(items)[count])
						engine.speak(list(items)[count], True)
					if event.key == pygame.K_UP:
						if count > 0:
							count = count-1
						if platform.system().lower() == "darwin":
							engine.voice("com.apple.speech.synthesis.voice."+list(items)[count])
						else:
							engine.voice(list(items)[count])
						engine.speak(list(items)[count], True)
					if event.key == pygame.K_RETURN:
						running = False
		if platform.system().lower() == "darwin":
			return "com.apple.speech.synthesis.voice."+list(items)[count]
		else:
			return list(items)[count]

	def rateSelector(self, engine, intro):
		self.sr.speak(intro)
		r = self.default_rate
		while True:
			time.sleep(.100)
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						engine.speak("This is a test paragraph, to test the rate of the selected voice..", True)
					if event.key == pygame.K_LEFT:
						if platform.system() == "Windows":
							r = r - 1
							if r < -10:
								r = -10
						else:
							if r < 50:
								r = 50
						engine.set_rate(r)
						self.sr.speak("Rate " + str(r), True)
					if event.key == pygame.K_RIGHT:
						if platform.system() == "Windows":
							r = r + 1
							if r > 10:
								r = 10
						else:
							if r > 450:
								r = 450
						engine.set_rate(r)
						self.sr.speak("Rate " + str(r), True)
					if event.key == pygame.K_RETURN:
						return r

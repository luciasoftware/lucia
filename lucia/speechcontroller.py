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

import platform, os
from .utils.ui import *
from accessible_output2.outputs.sapi5 import *

class SpeechController():
	def __init__(self):
		#---Check for Microsoft Speech API 5.x---#
		if platform.system() == "Windows":
			self.engine = SAPI5()
			return

			#---Check for NS Speech Synthesizer---#
		if platform.system() == "Darwin":
			try:
				from AppKit import NSSpeechSynthesizer
				from .steel.NSSS import NSSS
				self.engine = NSSS()
				return
			except ImportError:
				try:
					from Cocoa import NSSpeechSynthesizer
					from .steel.NSSS import NSSS
					self.engine = NSSS()
					return
				except:
					pass

		#---Check for eSpeak---#
		if platform.system() != "Windows" and platform.system() != "Darwin":
			if os.path.isdir("/usr/share/espeak-data") or os.path.isdir(os.path.join(os.path.expanduser("~/"),"espeak-data")):
				from .steel.eSpeak import eSpeak
				self.engine = eSpeak()

	def speak(self, text, interrupt=False, wait=False):
		display_text(str(text))
		self.engine.speak(str(text), interrupt)

	def stop(self):
		self.engine.stop()

	def get_available_voices(self):
		if platform.system() == "Windows":
			return self.engine.list_voices()
		else:
			return self.engine.available_voices()

	def set_rate(self, rate):
		if platform.system() == "Windows":
			self.engine.set_rate(int(rate))
		else:
			self.engine.set("rate", int(rate))

	def get_rate(self):
		if platform.system() == "Windows":
			self.engine.get_rate()
		else:
			self.engine.get("rate")

	def set_volume(self, volume):
		if platform.system() == "Windows":
			self.engine.set_volume(volume)
		else:
			self.engine.set("volume", volume)

	def get_volume(self):
		if platform.system() == "Windows":
			self.engine.get_volume()
		else:
			self.engine.get("volume")

	def set_voice(self, voice):
		if platform.system() == "Windows":
			self.engine.set_voice(voice)
		else:
			self.engine.set("voice", voice)

	def get_voice(self):
		if platform.system() == "Windows":
			self.engine.get_voice()
		else:
			self.engine.get("voice")

	def set_pitch(self, pitch):
		if platform.system() == "Windows":
			self.engine.set_pitch(pitch)
		else:
			self.engine.set("pitch", int(pitch))

	def get_pitch(self):
		if platform.system() == "Windows":
			self.engine.get_pitch()
		else:
			self.engine.get("pitch")

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

import pygame

def get_key():
	while True:
		event = pygame.event.poll()
		if event.type == pygame.KEYDOWN:
			return event.key
		else:
			pass

def simple_input(speech, intro, password=False):
	current_string = ""
	speech.speak(intro)
	while True:
		inkey = get_key()
		print(inkey)
		if inkey == pygame.K_BACKSPACE and current_string != "":
			if password:
				speech.speak("Star deleted", True)
			else:
				speech.speak(current_string[len(current_string)-1], + " deleted", True)
			current_string = current_string[0:-1]
		elif inkey == pygame.K_RETURN:
			break
		elif inkey == pygame.K_MINUS:
			current_string = current_string + "_"
		elif inkey <= 127:
			current_string= current_string + chr(inkey)
			if password:
				speech.speak("Star", True)
			else:
				speech.speak(chr(inkey), True)
	return current_string

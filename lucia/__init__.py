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

"""The main Lucia module

The functions here are responsible for initializing and quitting lucia, showing the game window, handle global events and so on.
In addition, this part of lucia also contains most keyboard functions.
"""

import os
import platform

os_bit, os_name = platform.architecture()
os.environ["PYAL_DLL_PATH"] = os.path.join(
	os.path.dirname(os.path.realpath(__file__)), "lib", os_bit
)
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

import sys
import pygame
from pygame.locals import *

# import subpackages..
from . import audio, ui

# import submodules
from .output import *
from .packfile import *


window = None
audio_backend = None
audio_backend_class = None
running = False
current_key_pressed = -1
current_key_released = -1
old_keys_held = []
keys_held = []
_resource_file = None
f4key = False
altkey = False


class AudioBackendException(ValueError):
	pass


class AudioBackend:
	OPENAL = 0
	BASS = 1
	FMOD = 2


def initialize(audiobackend=AudioBackend.BASS):
	"""Initialize lucia and the underlying graphic, audio, keyboard, interface engines"""
	global audio_backend, audio_backend_class, running
	pygame.init()
	# Set the pygame constants in lucia's namespace.
	from pygame import locals
	if audiobackend == AudioBackend.OPENAL:
		from .audio import openal as backend_openal

		audio_backend_class = backend_openal.OpenALAudioBackend()
		audio_backend_class.initialize()
		audio_backend = backend_openal
	if audiobackend == AudioBackend.BASS:
		from .audio import bass as backend_bass

		audio_backend_class = backend_bass.BassAudioBackend()
		audio_backend_class.initialize()
		audio_backend = backend_bass
	if audiobackend == AudioBackend.FMOD:
		raise AudioBackendException("FMOD backend not implemented yet.")
	running = True


def quit():
	"""Shutdown lucia and close underlying engines freeing up system resources"""
	audio_backend_class.quit()
	pygame.quit()


def get_global_resource_file():
	global _resource_file
	return _resource_file


def set_global_resource_file(file):
	global _resource_file
	if not isinstance(file, ResourceFile):
		raise ValueError('"file" must be an instance of "lucia.ResourceFile".')
	_resource_file = file


def show_window(title="LuciaGame", size=(640, 480)):
	"""Shows the main game window on the screen, this is most likely called at the start of a game"""
	global window
	window = pygame.display.set_mode(size)
	pygame.display.set_caption(title)
	return window


def process_events():
	"""This processes events for the window
	This should be called in any loop, to insure that the window and application stays responsive"""
	global current_key_pressed, current_key_released, old_keys_held, keys_held, running, window, audio_backend, altkey, f4key
	current_key_pressed = -1
	current_key_released = -1
	old_keys_held = keys_held
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			running = False
			quit()
			sys.exit(0)
			break
		# update key state here
		keys_held = ()
		keys_held = pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if platform.system() == "Windows": # check for alt f4
				if event.key==pygame.K_RALT or event.key==pygame.K_LALT:
					altkey=True
				elif event.key==pygame.K_F4:
					f4key=True
			if len(old_keys_held) > 0 and old_keys_held[event.key] == False:
				current_key_pressed = event.key
		if event.type == pygame.KEYUP:
			if platform.system() == "Windows": # check for alt f4
				if event.key==pygame.K_RALT or event.key==pygame.K_LALT:
					altkey=False
				elif event.key==pygame.K_F4:
					f4key=False
			current_key_released = event.key
	if altkey and f4key:
		running = False
		quit()
		sys.exit()
	pygame.display.update()
	audio_backend_class.update_audio_system()
	return events


def key_pressed(key_code):
	"""Checks if a key was pressed down this frame (single key press)
	* key_code: A pygame.K_ key code
	
	returns: True if the specified key kode was pressed, False otherwise.
	"""
	global current_key_pressed
	return current_key_pressed == key_code


def key_released(key_code):
	"""Checks if a key was released down this frame (single key release)
	* key_code: A pygame.K_ key code
	
	returns: True if the specified key kode was released, False otherwise.
	"""
	global current_key_released
	return current_key_released == key_code


def key_down(key_code):
	"""Checks if a key is beeing held down.
	* key_code: A pygame.K_ key code
	
	returns: True if the specified key kode is beeing held down, False otherwise.
	"""
	global keys_held
	return keys_held[key_code]


def key_up(key_code):
	"""Check if a key isn't beeing held down (ie if it's not pressed and held)
	* key_code : A pygame.K_ key code
	
	returns: True if key is not held down, False otherwise
	"""
	global keys_held
	return keys_held[key_code] == False

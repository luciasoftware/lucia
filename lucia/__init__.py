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
In addition, this part of lucia also contains must keyboard functions.
"""

import os
os.environ["PYAL_DLL_PATH"] = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(os.path.realpath(__file__))

import sys
import sdl2
import sdl2.ext
from sdl2.keycode import *

# import subpackages..
from . import audio, ui, utils

# import submodules
from .output import *
from .resourcemanager import *


window = None
audio_backend = None
running = False
current_key_pressed = 0
current_key_released = 0
keys_held = []

class AudioBackendNotSupportedException(ValueError):
	pass

class AudioBackend():
	OPENAL = 0
	BASS = 1
	FMOD = 2

def initialize(audiobackend=AudioBackend.OPENAL):
	"""Initialize lucia and the underlying graphic, audio, interface engines"""
	"""Initialize the underlying engines"""
	global audio_backend, running
	sdl2.ext.init()
	if audiobackend == AudioBackend.OPENAL:
		from .audio import openal as backend_openal
		backend_openal.initialize()
		audio_backend = backend_openal
	if audiobackend == AudioBackend.BASS:
		raise AudioBackendNotSupportedException("BASS backend not implemented yet.")
	if audiobackend == AudioBackend.FMOD:
		raise AudioBackendNotSupportedException("FMOD backend not implemented yet.")
	print(audio_backend)
	running = True

def quit():
	"""Shutdown lucia and close underlying engines freeing up system resources"""
	sdl2.ext.quit()

def show_window(title="LuciaGame", size=(640,480), **kwargs):
	"""Shows the main game window on the screen, this is most likely called at the start of a game"""
	global window
	window = sdl2.ext.Window(title, size, *kwargs)
	window.show()
	return window

def process_events():
	"""This processes events for the window
	This should be called in any loop, to insure that the window and application stays responsive"""
	global current_key_pressed, current_key_released, running, window, audio_backend
	current_key_pressed = 0
	current_key_released = 0
	events = sdl2.ext.get_events()
	for event in events:
		if event.type == sdl2.SDL_QUIT:
			running = False
			# for now just exit, in future call registered quit listeners.
			quit()
			sys.exit(0)
			break
		if event.type == sdl2.SDL_KEYDOWN:
			current_key_pressed = event.key.keysym.sym
			keys_held.append(event.key.keysym.sym)
		elif event.type == sdl2.SDL_KEYUP:
			current_key_released = event.key.keysym.sym
			for i in keys_held:
				if i==event.key.keysym.sym:
					keys_held.remove(i)
		window.refresh()
		audio_backend.update_audio_system()
	return events

def key_pressed(key_code):
	"""Checks if a key was pressed down this frame (single key press)
	* key_code: a lucia.SDLK key code
	
	returns: True if the specified key kode was pressed, False otherwise.
	"""
	global current_key_pressed
	return current_key_pressed == key_code

def key_released(key_code):
	"""Checks if a key was released down this frame (single key release)
	* key_code: a lucia.SDLK key code
	
	returns: True if the specified key kode was released, False otherwise.
	"""
	global current_key_released
	return current_key_released == key_code

def key_down(key_code):
	"""Checks if a key is beeing held down.
	* key_code: a lucia.SDLK key code
	
	returns: True if the specified key kode is beeing held down, False otherwise.
	"""
	global keys_held
	return key_code in keys_held

def key_up(key_code):
	"""Check if a key isn't beeing held down (ie if it's not pressed and held)
	key_code : An lucia.SDLK key code
	
	returns: True if key is not held down, False otherwise
	"""
	global keys_held
	return key_code not in keys_held

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
from . import audio, ui, utils

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


class AudioBackendException(ValueError):
	pass


class AudioBackend:
	OPENAL = 0
	BASS = 1
	FMOD = 2


def initialize(audiobackend=AudioBackend.OPENAL):
	"""Initialize lucia and the underlying graphic, audio, keyboard, interface engines"""
	"""Initialize the underlying engines"""
	global audio_backend, audio_backend_class, running
	pygame.init()
	__dict__["KEY_A"] = pygame.K_a
	__dict__["KEY_B"] = pygame.K_b
	__dict__["KEY_C"] = pygame.K_c
	__dict__["KEY_D"] = pygame.K_d
	__dict__["KEY_E"] = pygame.K_e
	__dict__["KEY_a"] = pygame.K_f
	__dict__["KEY_G"] = pygame.K_g
	__dict__["KEY_H"] = pygame.K_h
	__dict__["KEY_I"] = pygame.K_i
	__dict__["KEY_J"] = pygame.K_j
	__dict__["KEY_K"] = pygame.K_k
	__dict__["KEY_L"] = pygame.K_l
	__dict__["KEY_M"] = pygame.K_m
	__dict__["KEY_N"] = pygame.K_n
	__dict__["KEY_O"] = pygame.K_O
	__dict__["KEY_P"] = pygame.K_p
	__dict__["KEY_Q"] = pygame.K_q
	__dict__["KEY_R"] = pygame.K_r
	__dict__["KEY_S"] = pygame.K_s
	__dict__["KEY_T"] = pygame.K_t
	__dict__["KEY_U"] = pygame.K_u
	__dict__["KEY_V"] = pygame.K_v
	__dict__["KEY_W"] = pygame.K_w
	__dict__["KEY_X"] = pygame.K_x
	__dict__["KEY_Y"] = pygame.K_y
	__dict__["KEY_Z"] = pygame.K_z
	__dict__["KEY_UP"] = pygame.K_UP
	__dict__["KEY_DOWN"] = pygame.K_DOWN
	__dict__["KEY_LEFT"] = pygame.K_LEFT
	__dict__["KEY_RIGHT"] = pygame.K_RIGHT
	__dict__["KEY_RETURN"] = pygame.K_RETURN
	__dict__["KEY_BACK"] = pygame.K_BACKSPACE
	__dict__["KEY_TAB"] = pygame.K_TAB
	__dict__["KEY_CLEAR"] = pygame.K_CLEAR
	__dict__["KEY_PAUSE"] = pygame.K_PAUSE
	__dict__["KEY_ESCAPE"] = pygame.K_ESCAPE
	__dict__["KEY_SPACE"] = pygame.K_SPACE
	__dict__["KEY_EXCLAIM"] = pygame.K_EXCLAIM
	__dict__["KEY_QUOTEDBL"] = pygame.K_QUOTEDBL
	__dict__["KEY_HASH"] = pygame.K_HASH
	__dict__["KEY_DOLLAR"] = pygame.K_DOLLAR
	__dict__["KEY_AMPERSAND"] = pygame.K_AMPERSAND
	__dict__["KEY_QUOTE"] = pygame.K_QUOTE
	__dict__["KEY_LPAREN"] = pygame.K_LEFTPAREN
	__dict__["KEY_RPAREN"] = pygame.K_RIGHTPAREN
	__dict__["KEY_ASTERISK"] = pygame.K_ASTERISK
	__dict__["KEY_PLUS"] = pygame.K_PLUS
	__dict__["KEY_COMMA"] = pygame.K_COMMA
	__dict__["KEY_MINUS"] = pygame.K_MINUS
	__dict__["KEY_PERIOD"] = pygame.K_PERIOD
	__dict__["KEY_SLASH"] = pygame.K_SLASH
	__dict__["KEY_COLON"] = pygame.K_COLON
	__dict__["KEY_SEMICOLON"] = pygame.K_SEMICOLON
	__dict__["KEY_LESS"] = pygame.K_LESS
	__dict__["KEY_EQUALS"] = pygame.K_EQUALS
	__dict__["KEY_GREATER"] = pygame.K_GREATER
	__dict__["KEY_QUESTION"] = pygame.K_QUESTION
	__dict__["KEY_AT"] = pygame.K_AT
	__dict__["KEY_LBRACKET"] = pygame.K_LEFTBRACKET
	__dict__["KEY_RBRACKET"] = pygame.K_RIGHTBRACKET
	__dict__["KEY_BACKSLASH"] = pygame.K_BACKSLASH
	__dict__["KEY_CARET"] = pygame.K_CARET
	__dict__["KEY_UNDERSCORE"] = pygame.K_UNDERSCORE
	__dict__["KEY_GRAVE"] = pygame.K_BACKQUOTE
	__dict__["KEY_0"] = pygame.K_0
	__dict__["KEY_1"] = pygame.K_1
	__dict__["KEY_2"] = pygame.K_2
	__dict__["KEY_3"] = pygame.K_3
	__dict__["KEY_4"] = pygame.K_4
	__dict__["KEY_5"] = pygame.K_5
	__dict__["KEY_6"] = pygame.K_6
	__dict__["KEY_7"] = pygame.K_7
	__dict__["KEY_8"] = pygame.K_8
	__dict__["KEY_9"] = pygame.K_9
	__dict__["KEY_DEL"] = pygame.K_DELETE
	__dict__["KEY_KEYPAD0"] = pygame.K_KP0
	__dict__["KEY_KEYPAD1"] = pygame.K_KP1
	__dict__["KEY_KEYPAD2"] = pygame.K_KP2
	__dict__["KEY_KEYPAD3"] = pygame.K_KP3
	__dict__["KEY_KEYPAD4"] = pygame.K_KP4
	__dict__["KEY_Kp5"] = pygame.K_KP5
	__dict__["KEY_KP6"] = pygame.K_KP6
	__dict__["KEY_KP7"] = pygame.K_KP7
	__dict__["KEY_KP8"] = pygame.K_KP8
	__dict__["KEY_KP9"] = pygame.K_KP9
	__dict__["KEY_KEYPAD_PERIOD"] = pygame.K_KP_PERIOD
	__dict__["KEY_KEYPAD_DEVIDE"] = pygame.K_KP_DEVIDE
	__dict__["KEY_KEYPAD_MULTIPLY"] = pygame.K_KP_MULTIPLY
	__dict__["KEY_KEYPAD_MINUS"] = pygame.K_KP_MINUS
	__dict__["KEY_KEYPAD_PLUS"] = pygame.K_KP_PLUS
	__dict__["KEY_KEYPAD_ENTER"] = pygame.K_KP_ENTER
	__dict__["KEY_KEYPAD_EQUALS"] = pygame.K_KP_EQUALS
	__dict__["KEY_INSERT"] = pygame.K_INSERT
	__dict__["KEY_HOME"] = pygame.K_HOME
	__dict__["KEY_END"] = pygame.K_END
	__dict__["KEY_PAGEUP"] = pygame.K_PAGEUP
	__dict__["KEY_PAGEDOWN"] = pygame.K_PAGEDOWN
	__dict__["KEY_F1"] = pygame.K_F1
	__dict__["KEY_F2"] = pygame.K_F2
	__dict__["KEY_F3"] = pygame.K_F3
	__dict__["KEY_F4"] = pygame.K_F4
	__dict__["KEY_F5"] = pygame.K_F5
	__dict__["KEY_F6"] = pygame.K_F6
	__dict__["KEY_F7"] = pygame.K_F7
	__dict__["KEY_F8"] = pygame.K_F8
	__dict__["KEY_F9"] = pygame.K_F9
	__dict__["KEY_F10"] = pygame.K_F10
	__dict__["KEY_F11"] = pygame.K_F11
	__dict__["KEY_F12"] = pygame.K_F12
	__dict__["KEY_F13"] = pygame.K_F13
	__dict__["KEY_F14"] = pygame.K_F14
	__dict__["KEY_F15"] = pygame.K_F15
	__dict__["KEY_NUMLOCK"] = pygame.K_NUMLOCK
	__dict__["KEY_CAPSLOCK"] = pygame.K_CAPSLOCK
	__dict__["KEY_SCROLLOCK"] = pygame.K_SCROLLOCK
	__dict__["KEY_RSHIFT"] = pygame.K_RSHIFT
	__dict__["KEY_LSHIFT"] = pygame.K_LSHIFT
	__dict__["KEY_RCONTROL"] = pygame.K_RCTRL
	__dict__["KEY_LCONTROL"] = pygame.K_LCTRL
	__dict__["KEY_RALT"] = pygame.K_RALT
	__dict__["KEY_LALT"] = pygame.K_LALT
	__dict__["KEY_RMETA"] = pygame.K_RMETA
	__dict__["KEY_LMETA"] = pygame.K_LMETA
	__dict__["KEY_LWIN"] = pygame.K_LSUPER
	__dict__["KEY_RSUPER"] = pygame.K_RWIN
	__dict__["KEY_MODE"] = pygame.K_MODE
	__dict__["KEY_HELP"] = pygame.K_HELP
	__dict__["KEY_PRINTSCREEN"] = pygame.K_PRINT
	__dict__["KEY_SYSREQ"] = pygame.K_SYSREQ
	__dict__["KEY_BREAK"] = pygame.K_BREAK
	__dict__["KEY_MENU"] = pygame.K_MENU
	__dict__["KEY_POWER"] = pygame.K_POWER
	__dict__["KEY_EURO"] = pygame.K_EURO
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
		raise ValueError('"file" most be an instance of "lucia.ResourceFile".')
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
	global current_key_pressed, current_key_released, old_keys_held, keys_held, running, window, audio_backend
	current_key_pressed = -1
	current_key_released = -1
	old_keys_held = keys_held
	events = pygame.event.get()
	for event in events:
		if event.type == QUIT:
			running = False
			# for now just exit, in future call registered quit listeners.
			quit()
			sys.exit(0)
			break
		# update key state here
		keys_held = ()
		keys_held = pygame.key.get_pressed()
		if event.type == pygame.KEYDOWN:
			if len(old_keys_held) > 0 and old_keys_held[event.key] == False:
				current_key_pressed = event.key
		if event.type == pygame.KEYUP:
			current_key_released = event.key
		pygame.display.update()
		audio_backend_class.update_audio_system()
	return events


def key_pressed(key_code):
	"""Checks if a key was pressed down this frame (single key press)
	* key_code: a pygame.K_ key code
	
	returns: True if the specified key kode was pressed, False otherwise.
	"""
	global current_key_pressed
	return current_key_pressed == key_code


def key_released(key_code):
	"""Checks if a key was released down this frame (single key release)
	* key_code: pygame.K_ key code
	
	returns: True if the specified key kode was released, False otherwise.
	"""
	global current_key_released
	return current_key_released == key_code


def key_down(key_code):
	"""Checks if a key is beeing held down.
	* key_code: a pygame.K_ key code
	
	returns: True if the specified key kode is beeing held down, False otherwise.
	"""
	global keys_held
	return keys_held[key_code]


def key_up(key_code):
	"""Check if a key isn't beeing held down (ie if it's not pressed and held)
	key_code : An pygame.K_ key code
	
	returns: True if key is not held down, False otherwise
	"""
	global keys_held
	return keys_held[key_code] == False

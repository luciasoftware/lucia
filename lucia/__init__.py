"""The main Lucia module"""

import os
os.environ["PYAL_DLL_PATH"] = os.path.dirname(__file__)
os.environ["PYSDL2_DLL_PATH"] = os.path.dirname(__file__)

import sys
import sdl2
import sdl2.ext

# import subpackages..
from . import audio, interface, utils

# import submodules
from .output import *
from .resourcemanager import *


window = None
running = False
current_key_pressed = 0
current_key_released = 0
keys_held = []

def initialize():
	"""Initialize the underlying engines"""
	global running
	sdl2.ext.init()
	running = True

def show_window(title="LuciaGame", size=(700,600), **kwargs):
	"""Shows the main game window on the screen"""
	global window
	window = sdl2.ext.Window(title, size, *kwargs)
	window.show()
	return window

def process_events():
	"""This processes events for the window
	This should be called in any loop, to insure that the window and application stays responsive"""
	global current_key_pressed, current_key_released, running, window
	current_key_pressed = 0
	current_key_released = 0
	events = sdl2.ext.get_events()
	for event in events:
		if event.type == sdl2.SDL_QUIT:
			running = False
			# for now just exit, in future call registered quit listeners.
			sys.exit(0)
			break
		if event.type == sdl2.SDL_KEYDOWN:
			current_key_pressed = event.key.keysym.sym
			keys_held.append(event.key.keysym.sym)
		if event.type == sdl2.SDL_KEYUP:
			current_key_released = event.key.keysym.sym
			if event.key.keysym.sym in keys_held:
				keys_held.remove(event.key.keysym.sym)
		window.refresh()
	return sdl2.ext.get_events()

def key_pressed(key_code):
	global current_key_pressed
	return current_key_pressed == key_code

def key_released(key_code):
	global current_key_released
	return current_key_released == key_code

def key_down(key_code):
	global held_keys
	return key_code in held_keys

def key_up(key_code):
	global held_keys
	return key_code not in held_keys

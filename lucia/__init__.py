"""The main Lucia module"""

import os
os.environ["PYAL_DLL_PATH"] = os.path.dirname(__file__)

import sys
import pyglet
from pyglet.window import key

from . import audio, interface, utils


window = None
keyboard_handler = None

def initialize():
	"""Initialize the underlying engines"""

def show_window(**kwargs):
	"""Shows the main game window on the screen
	
	title : str
		Set the window title
	width : int
		Set the underlying window width.
	height : int
		Set the underlying window height.
	full_screen : book
		Boolean to set full screen mode (True for full screen, False for windowed)
	"""
	global window, keyboard_handler
	window = pyglet.window.Window(**kwargs)
	keyboard_handler = key.KeyStateHandler()
	window.push_handlers(keyboard_handler)
	return window

def make_keyboard_exclusive():
	"""Makes all keys (including windows, tab+alt and so on) go to the application instead of the os"""
	global window
	window.set_exclusive_keyboard()

def is_key_down(key_code):
	"""Check if a key is held down
	
	key : pyglet.window.key
		A pyglet.window.key code like key.SPACE, or key.A
	"""
	return True if key in keyboard_handler else False

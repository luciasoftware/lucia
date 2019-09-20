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

"""advanced menu for advanced use

this menu module provides highly flexible menu items with different events and an advanced menu handling"""

import sys
import time

import lucia
from lucia.ui.virtualinput import *

# Events
CANCELEVENT = 0


def getinput(title, message, multiline=False, value="", mode="plaintext"):
	if mode == "plaintext":
		if multiline:
			input = VirtualInput("enter value", value=value)
		else:
			input = VirtualInput("enter value", value=value)
			# Later this will have multilinebox enabled so this condition remains still
	elif mode == "spinbox":
		input = VirtualInput("enter value", whitelist=WHITELIST_DIGITS, value=value)
	text = input.run()
	return text


class MenuItem:
	def __init__(
		self,
		name,
		can_return=False,
		has_value=False,
		value="",
		value_mode="plaintext",
		can_be_toggled=False,
		toggle_value=False,
		can_activate=True,
		item_function=None,
		on_focus=None,
		event=None,
	):
		self.name = name
		self.has_value = has_value
		self.value_mode = value_mode
		self.value = value
		self.can_be_toggled = can_be_toggled
		self.toggle_value = toggle_value
		self.can_return = can_return
		self.can_activate = can_activate
		self.item_function=item_function #this should be a function. It is called when the item is clicked. If the item is able to return and the event property isn't set to CANCELEVENT, instead of breaking out of the loop, just a function gets called. If the event property is set to CANCELEVENT the function gets called, but it'll break out of the loop too. This way you can make virtual submenus too except that you can switch between parent and child menus with left and right
		self.on_focus = on_focus #a function that is called whenever the focus is on this item
		self.event = event #Usually an integer. See the events section



class Menu:
	def __init__(
		self,
		items,
		clicksound="",
		edgesound="",
		wrapsound="",
		entersound="",
		opensound="",
		itempos=0,
		title="menu",
		fpscap=120,
		on_index_change=None,
		callback_function=None,
	):
		self.clicksound = clicksound
		self.edgesound = edgesound
		self.wrapsound = wrapsound
		self.entersound = entersound
		self.opensound = opensound
		self.itempos = itempos
		self.items = items
		self.title = title
		self.fpscap = fpscap
		self.on_index_change = on_index_change # make sure this is a function. It is called whenever the index of a menu is changed. The index change happens whenever user cycles between menu items.
		self.callback = callback_function # This should be a function. This function is called within the menu loop
		self.pool = lucia.audio_backend.SoundPool()

	def run(self):
		"""when this function is called, menu loop starts. If the user make the menu return such as pressing enter on an item that has can_return attribute set to true the loop ends and it usually returns results as a list of dictionaries"""
		try:
			lucia.output.speak(self.title)
			return self.loop()
		except Exception as e:
			lucia.output.speak(str(e))

	def loop(self):
		while 1:
			time.sleep(0.001)
			try:
				lucia.process_events()
				if callable(self.callback):
					self.callback()
				if lucia.key_pressed(lucia.K_RETURN):
					if self.items[self.itempos].can_return:
						if self.entersound != "":
							source = self.pool.play_stationary(self.entersound)
						list_values = []
						if self.items[self.itempos].event == CANCELEVENT:
							if callable(self.items[self.itempos].item_function):
								self.items[self.itempos].item_function()
							return list_values
						#returns results as a list of dictionaries. The currently focused item returns as the first item in the list
						for x in self.items:
							if x.name != self.items[self.itempos].name:
								list_values.append(
									{"name": x.name, "value": x.value, "toggle_value": x.toggle_value}
								)
						list_values.insert(
							0,
							{
								"name": self.items[self.itempos].name,
								"value": self.items[self.itempos].value,
								"toggle_value": self.items[self.itempos].toggle_value,
							},
						)
						if callable(self.items[self.itempos].item_function):
							self.items[self.itempos].item_function()
						else:
							return list_values
				elif lucia.key_pressed(lucia.K_UP):
					if self.itempos > 0:
						self.itempos -= 1
						if self.clicksound != "":
							clicksound = self.pool.play_stationary(self.clicksound)
						if callable(self.on_index_change):
							self.on_index_change()
						if callable(self.items[self.itempos].on_focus):
							self.items[self.itempos].on_focus(self)
						if (
							self.items[self.itempos].has_value == False
							and self.items[self.itempos].can_be_toggled == False
						):
							lucia.output.speak(self.items[self.itempos].name)
						elif (
							self.items[self.itempos].has_value
							and self.items[self.itempos].can_be_toggled == False
						):
							lucia.output.speak(
								self.items[self.itempos].name
								+ ": "
								+ str(self.items[self.itempos].value)
								+ ". Press left shift or right shift to change this item's value"
							)
						elif (
							self.items[self.itempos].has_value == False
							and self.items[self.itempos].can_be_toggled
						):
							if self.items[self.itempos].toggle_value == True:
								lucia.output.speak(
									self.items[self.itempos].name + ": On. Press space to switch off"
								)
							else:
								lucia.output.speak(
									self.items[self.itempos].name + ": Off. Press space to switch on"
								)
						elif (
							self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled
						):
							speakstr = (
								self.items[self.itempos].name
								+ ". Value: "
								+ str(self.items[self.itempos].value)
							)
							if self.items[self.itempos].toggle_value == True:
								speakstr += ". Switch: On"
							else:
								speakstr += ". Switch: Off"
							lucia.output.speak(
								speakstr
								+ ". Press left shift or right shift to change this item's value. Press space to toggle on or off"
							)
				elif lucia.key_pressed(lucia.K_DOWN):
					if self.itempos < len(self.items) - 1:
						self.itempos += 1
						if self.clicksound != "":
							clicksound = self.pool.play_stationary(self.clicksound)
						if self.items[self.itempos].on_focus != None:
							self.items[self.itempos].on_focus()
						if self.on_index_change != None:
							self.on_index_change()
						if (
							self.items[self.itempos].has_value == False
							and self.items[self.itempos].can_be_toggled == False
						):
							lucia.output.speak(self.items[self.itempos].name)
						elif (
							self.items[self.itempos].has_value
							and self.items[self.itempos].can_be_toggled == False
						):
							lucia.output.speak(
								self.items[self.itempos].name
								+ ": "
								+ str(self.items[self.itempos].value)
								+ ". Press left shift or right shift to change this item's value"
							)
						elif (
							self.items[self.itempos].has_value == False
							and self.items[self.itempos].can_be_toggled
						):
							if self.items[self.itempos].toggle_value == True:
								lucia.output.speak(
									self.items[self.itempos].name + ": On. Press space to switch off"
								)
							else:
								lucia.output.speak(
									self.items[self.itempos].name + ": Off. Press space to switch on"
								)
						elif (
							self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled
						):
							speakstr = (
								self.items[self.itempos].name
								+ ". Value: "
								+ str(self.items[self.itempos].value)
							)
							if self.items[self.itempos].toggle_value == True:
								speakstr += ". Switch: On"
							else:
								speakstr += ". Switch: Off"
							lucia.output.speak(
								speakstr
								+ ". Press left shift or right shift to change this item's value. Press space to toggle on or off"
							)
				elif lucia.key_pressed(lucia.K_SPACE):
					if self.itempos > -1 and self.itempos < len(self.items):
						if self.items[self.itempos].can_be_toggled:
							if self.entersound != "":
								entersound = self.pool.play_stationary(self.entersound)
							if self.items[self.itempos].toggle_value == True:
								lucia.output.speak("off")
								self.items[self.itempos].toggle_value = False
							else:
								lucia.output.speak("on")
								self.items[self.itempos].toggle_value = True
				elif lucia.key_down(lucia.K_LSHIFT) or lucia.key_down(lucia.K_RSHIFT):
					if self.items[self.itempos].has_value == True:
						self.items[self.itempos].value = getinput(
							"change value",
							self.items[self.itempos].name + ". ",
							value=self.items[self.itempos].value,
							mode=self.items[self.itempos].value_mode,
						)
						lucia.output.speak("value set to " + str(self.items[self.itempos].value))
						if self.entersound != "":
							entersound = self.pool.play_stationary(self.entersound)
			except Exception as e:
				lucia.output.speak(str(e))

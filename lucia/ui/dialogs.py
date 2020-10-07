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

"""A module providing the ability to prompt the user for varying input and for displaying any message
"""

import lucia
import string
from lucia.utils import timer
class message_dialog:
	def __init__(self, message='message'):
		self.message=message
		self.running=False
	def run(self):
		lucia.output.output(self.message)
		self.running=True
		while self.running:
			lucia.process_events()
			if lucia.key_pressed(lucia.K_UP) or lucia.key_pressed(lucia.K_DOWN) or lucia.key_pressed(lucia.K_LEFT) or lucia.key_pressed(lucia.K_RIGHT):
				lucia.output.output(self.message)
			if lucia.key_pressed(lucia.K_RETURN) or lucia.key_pressed(lucia.K_ESCAPE):
				self.running=False

class virtualInput:
	def __init__(self, initial_msg = "", password = False, password_msg = "*", repeat_chars = True, repeat_keys = False, enter = True, msg_length = -1, repeat_first_ms = 500, repeat_second_ms = 50):
		"""Initializes the virtual input:
		Parameters:
			initial_msg (str): The initial contents of the input string
			password (bool): Dictates whether the characters will be spoken
			password_msg (str): The string spoken should the input be hidden
			repeat_chars (bool): Dictates whether the characters will be echoed back as the user types
			repeat_keys (bool): Dictates whether the characters will be repeated after a certain length of time holding down the key
			enter (bool): Determines if the user can press enter to exit the input
			msg_length (int): Sets the maximum character limit one wishes to have in the string before returning
			repeat_first_ms (int): Determines the first instance after which the user's keys will be automatically held. Best left at 500 so the user would have to trigger this event intentionally
			repeat_second_ms (int): Time waited after the first event fires. I.e, assuming the first_ms = 500, the keys will first be repeated at 500, then 550, 600, etc.
		"""
		self.current_string = initial_msg
		self._cursor = max(0, len(self.current_string) - 1)
		self.hidden = password
		self.password_message = password_msg
		self.repeating_characters = repeat_chars
		self.repeating_keys = repeat_keys
		self.can_exit = enter
		#Toggle this to true within your input callback to break out of input
		self.should_break = False
		self.whitelisted_characters = [a for a in string.printable]
		self.maximum_message_length = msg_length
		self._key_times = {}
		self.key_repeat_timer = timer.Timer()
		self.initial_key_repeating_time = repeat_first_ms
		self.repeating_increment = repeat_second_ms

	#Determines whether the run function should break out of it's loop
	@property
	def is_at_character_limit(self):
		if self.should_break:
			return True
		return False if self.maximum_message_length == -1 or len(self.current_string) < self.maximum_message_length else True

	@property
	def current_text(self):
		return self.current_string

	@current_text.setter
	def current_text(self, text):
		self.current_string = current_text
		self._cursor = max(0, len(self._current_string) - 1)

	def clear(self):
		"""Resets the input. This can be called outside of the class, but run will also do this internally upon every call
		"""
		self.current_string = ""
		self._cursor = 0
		self._key_times = {}
		self.key_repeat_timer.restart()

	def move_in_string(self, value):
		"""Moves in a string. Used when the user presses left and right arrow keys
		Parameters:
			value (int): The value by which the cursor will be moved
		"""
		self._cursor += value
		if self._cursor < 0: self._cursor = 0
		elif self._cursor > len(self.current_string): self._cursor = len(self.current_string)

	def get_character(self):
		"""Retrieves the character at the cursor's position
		Return Value:
			A single character if the cursor is in the bounds of the string and the string is not empty, empty string otherwise
		"""
		return "" if len(self.current_string) == 0 or self._cursor == len(self.current_string) else self.current_string[self._cursor]

	def insert_character(self, character):
		"""Inserts a character into the text
		Parameters:
			character (str): The character to be inserted
		"""
		if len(character) == 0: return
		self.current_string = self.current_string[:max(0, self._cursor)] + character + self.current_string[max(0, self._cursor):] if self._cursor < len(self.current_string) else self.current_string + character
		self._cursor += len(character)
		self.speak_character(character)

	def remove_character(self):
		"""Removes a character from the string based upon the cursor's position
		"""
		if self._cursor == 0: return
		self.speak_character(self.current_string[self._cursor - 1])
		if self._cursor == len(self.current_string):
			self.current_string = self.current_string[:-1]
		else:
			self.current_string = self.current_string[:self._cursor - 1] + self.current_string[self._cursor:]
		self._cursor -= 1

	def speak_character(self, character):
		"""Outputs a given character respective the repeating_characters and password settings
		Parameters:
			character (str): The character to be outputted
		"""
		if not self.repeating_characters: return
		if self.hidden: lucia.output.output(self.password_message)
		else: lucia.output.output(character)

	def snap_to_top(self):
		"""Snaps to the top of text (0 on the cursor position)
		"""
		self._cursor = 0
		self.speak_character(self.get_character(), True)

	def snap_to_bottom(self):
		"""Snaps to the bottom of text (len(self.current_string))
		"""
		self._cursor = len(self.current_string)
		self.speak_character(self.get_character(), True)

	def toggle_input_to_letters(self):
		"""Toggles the input to select only ascii letters
		"""
		self.whitelisted_characters = [a for a in string.ascii_letters]

	def toggle_input_to_digits(self, negative = False, decimal = False):
		"""Toggles the input to select only ascii digits
		Parameters:
			negative (bool): Dictates whether the user can type in a dash (-)
			decimal (bool): Dictates whether a user can type in a period (.)
		"""
		self.whitelisted_characters = [a for a in string.digits]
		if negative: self.whitelisted_characters.append("-")
		if decimal: self.whitelisted_characters.append(".")

	def toggle_input_to_all(self):
		"""Toggles the input to accept all printable characters
		"""
		self.whitelisted_characters = [a for a in string.printable if not i == "\r" or i == "\n"]

	def toggle_input_to_custom(self, characters):
		"""Toggles the input to select user-provided input
		Parameters:
			characters (str): A string of characters the user wishes to allow the input to accept
		"""
		self.whitelisted_characters = [a for a in characters]

	def run(self, message, callback = None):
		"""Retrieves user input
		Parameters:
			message (str): The message to be shown as the input pops up
			callback (callable): What will be called every iteration of the input loop. The input will pass in itself as the only parameter to the callback
		Return Value:
			self.current_text (str): What the user entered
		"""
		lucia.output.output(message, True)
		self.clear()
		while not self.is_at_character_limit:
			events = lucia.process_events()
			if callable(callback): callback(self)
			for event in events:
				if event.type == lucia.KEYDOWN:
					if self.repeating_keys and event.key not in self._key_times: self._key_times[event.key] = [self.key_repeat_timer.elapsed + self.initial_key_repeating_time, event.unicode]
					if self.can_exit and event.key == lucia.K_RETURN:
						return self.current_text
					elif event.key == lucia.K_BACKSPACE: self.remove_character()
					elif event.key == lucia.K_TAB: lucia.output.output(self.current_string, True)
					elif event.key == lucia.K_LEFT:
						self.move_in_string(-1)
						self.speak_character(self.get_character())
					elif event.key == lucia.K_RIGHT:
						self.move_in_string(1)
						self.speak_character(self.get_character())
					elif event.key == lucia.K_HOME:
						self.snap_to_top()
					elif event.key == lucia.K_END:
						self.snap_to_bottom()
					elif event.key == lucia.K_F2:
						lucia.output.output("Character repeat on") if self.toggle_character_repetition() else lucia.output.output("Character repeat off")
					else:
						if event.unicode in self.whitelisted_characters: self.insert_character(event.unicode)
				elif event.type == lucia.KEYUP:
					if event.key in self._key_times: del self._key_times[event.key]
			for key in self._key_times:
				if self.key_repeat_timer.elapsed >= self._key_times[key][0]:
					self._key_times[key][0] += self.repeating_increment
					lucia.pygame.event.post(lucia.pygame.event.Event(lucia.KEYDOWN, key = key, unicode = self._key_times[key][1]))
			lucia.pygame.time.wait(2)
		return self.current_text

	def get_integer_input(self, message, callback = None, negative = False, decimal = False):
		"""Gets the input from the user and tries to convert it to integer. Will toggle itself to the previous input mode regardless of the result
		Parameters:
			message (str): See the run function
			callback (callable): See the run function
			negative (bool): See the toggle_input_to_digits function
			decimal (bool): See the toggle_input_to_digits function
		Return Value:
			A number upon success, None on failure
		"""
		temp = "".join(self.whitelisted_characters)
		self.toggle_input_to_digits(negative, decimal)
		try:
			number = int(self.run(message, callback))
		except ValueError:
			number = None
		self.toggle_input_to_custom(temp)
		return number

	def get_list_input(self, messages, callbacks = []):
		"""Allows the user to queue several messages in a row.
		Parameters:
			messages (list): The messages passed along to the run function as each prompt gets processed
			callbacks (list): Will be passed to the run function with the same indexes as the messages. If fewer callbacks are passed, None will be substituted
		"""
		responses = []
		for i in range(len(messages)):
			if i < len(callbacks) - 1: result = self.run(messages[i], callbacks[i])
			else: result = self.run(messages[i])
			responses.append(result)
		return responses

	def get_integer_list_input(self, messages, callbacks = [], negative = False, decimal = False):
		"""Allows the user to queue several messages in a row requesting for integers. Will reset input to the previous mode regardless of success or failure
		Parameters:
			messages (list): See the  get_list_input function
			callbacks (list): See the get_list_input function
			negative (bool): See the toggle_input_to_digits function
			decimal (bool): See the toggle_input_to_digits function
		Return Value:
			A list of processed integers regardless of failure
		"""
		#A bit repetitive, but must do it as we don't want to join strings every time we process an int
		temp = "".join(self.whitelisted_characters)
		self.toggle_input_to_digits(negative, decimal)
		results = []
		for i in range(len(messages)):
			try:
				if i < len(callbacks) - 1:
					results.append(int(self.run(messages[i], callbacks[i])))
				else:
					results.append(self.run(messages[i]))
			except ValueError:
				break
		self.toggle_input_to_custom(temp)
		return results
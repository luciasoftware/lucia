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

import time


class Timer:
	"""A timer class, to track time mesured in millis
	"""

	def __init__(self):
		self.inittime = int(round(time.time() * 1000))

	def elapsed(self):
		"""Returns the exact elapsed time since this timer was created or last restarted.
		"""
		return int(round(time.time() * 1000)) - self.inittime

	def restart(self):
		"""Restarts the timer, and set it's elapsed time to 0.
		"""
		self.inittime = int(round(time.time() * 1000))

	def force(self, amount):
		"""Sets the timer to a specific time.
		
		Args:
			amount (int): The time to set to this timer (in millis)
		"""
		self.inittime = amount - ((int(round(time.time())) * 1000) - self.inittime)

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
		self.inittime = time.time()

	@property
	def elapsed(self):
		"""Returns the exact elapsed time since this timer was created or last restarted.
		"""
		return self._ms(time.time() - self.inittime)

	@elapsed.setter
	def elapsed(self, amount):
		"""Forces the timer to a specific time.
		
		Args:
			amount (int): The time elapsed (in millis)
		"""
		self.inittime = time.time() - (amount / 1000)

	def restart(self):
		"""Restarts the timer, and set it's elapsed time to 0.
		"""
		self.__init__()

	def _ms(self, t):
		return int(round(t*1000))

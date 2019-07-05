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

from abc import ABC, abstractmethod


class Sound(ABC):
	@abstractmethod
	def load(*args, **kwargs):
		pass

	@abstractmethod
	def play(*args, **kwargs):
		pass

	@abstractmethod
	def pause(*args, **kwargs):
		pass

	@abstractmethod
	def resume(*args, **kwargs):
		pass

	@abstractmethod
	def get_source_object(*args, **kwargs):
		pass

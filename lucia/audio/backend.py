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


class AudioBackend(ABC):
	@abstractmethod
	def initialize(self):
		pass

	@abstractmethod
	def update_audio_system(self):
		pass

	@abstractmethod
	def quit(self):
		pass

	@abstractmethod
	def is_hrtf_compatible(self):
		pass

	@abstractmethod
	def enable_hrtf(self, should_enable):
		pass


class BackActionNotSupported(ValueError):
	pass

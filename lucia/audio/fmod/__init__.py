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

import lucia
import pyfmode

system = None


class FMODAudioBackend(lucia.audio.AudioBackend):
	def initialize(self):
		global system
		system = pyfmodex.System()
		system.init()

	def quit(self):
		global system
		system.close()

	def is_hrtf_compatible(self):
		return False

	def enable_hrtf(self, should_enable):
		raise lucia.audio.BackActionNotSupported(
			"ENabling HRTF back wide is not available with the FMOD backend"
		)

	def update_audio_system(self):
		global system
		system.update()

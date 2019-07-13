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
from .sound import *
from .soundpool import *

from sound_lib import output

generic_output = None  # used for sounds objects.


class BassAudioBackend(lucia.audio.AudioBackend):
	def initialize(self):
		global generic_output
		generic_output = (
			output.Output()
		)  # initializing default output because the 3d one doesnt work.
		generic_output.start()

	def quit(self):
		global generic_output
		generic_output.stop()
		generic_output = None

	def is_hrtf_compatible(self):
		return False

	def enable_hrtf(self, should_enable):
		raise lucia.audio.BackActionNotSupported(
			"Enabling HRTF is not available with the Bass backend"
		)

	def update_audio_system(self):
		pass

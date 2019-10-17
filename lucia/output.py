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

import platform
import os

# import ao2, check for Runtime Error (missing espeak binaries on ReadTheDocs).
try:
	from accessible_output2.outputs.auto import *
	output = Auto()
	"""
	Functions:
	get_first_available_output() - autoselects the first available output.
	speak(text, interrupt=False) - speaks some text.
	silence() - Silence the current output if speaking.
	braille(text, **options) - braills some output.
	output(text, *args) - Both speak and braille some text.
	is_active() - checks if the given output is active.
	"""
except RuntimeError:
	if platform.system() == "Linux" and "readthedocs.org" in os.getcwd():
		pass
	else:
		raise


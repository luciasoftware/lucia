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

# this is a simple testing game, used to show the features of lucia.
# Add this repository's lucia package to the PYTHON PATH, so this example can find the lucia module.
import sys

sys.path.append(".")
print("Importing lucia")
import lucia

print("Initializing lucia")
lucia.initialize(audiobackend=lucia.AudioBackend.BASS)
print("Showing the window")
test = lucia.show_window()

print("importing menu2")
from lucia.ui import menu2

print("Making menu")
MenuItems = [
	menu2.MenuItem("hello"),
	menu2.MenuItem("world", has_value=True),
	menu2.MenuItem("this is a "),
	menu2.MenuItem("test", can_be_toggled=True),
	menu2.MenuItem("exit", True),
]
menu = menu2.Menu(items=MenuItems, title="test menu")
result = menu.run()
if result[0]["name"] == "exit":
	print(str(result))
	lucia.quit()
	exit()

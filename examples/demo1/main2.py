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
import wx
print("Importing lucia")
import lucia

print("Initializing lucia")
lucia.initialize()
app=wx.App()
print("Showing the window")
test = lucia.show_window()
app.MainLoop()
print("importing menu2")
from lucia.ui import menu2
print("Making menu")
menuitems=[menu2.menuitem("hello"), menu2.menuitem("world"), menu2.menuitem("this is a "), menu2.menuitem("test")]
menu = menu2.Menu(items=menuitems, title="test menu")
result = menu.run()
print(str(result))

while lucia.running:
	lucia.process_events()

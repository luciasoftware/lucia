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

sys.path.append("../..")

print("Importing lucia")
import lucia

print("Initializing lucia")
lucia.initialize(audiobackend=lucia.AudioBackend.OPENAL)

print("Showing the window")
test = lucia.show_window()

print("Making menu")
def callback_test(menu):
	print("hello world")

menu = lucia.ui.Menu()
menu.add_item_tts("Hello")
menu.add_item_tts("world")
menu.add_item_tts("this")
menu.add_item_tts("is")
menu.add_item_tts("a")
menu.add_item_tts("test")
menu.set_callback(callback_test)
result = menu.run("Please select something")
print(str(result))

username = lucia.ui.VirtualInput("Enter a username")
result = username.run()
print(f"username: {result}")
password = lucia.ui.VirtualInput("Enter a password", True)
result = password.run()
print(f"password: {result}")

while True:
	lucia.process_events()
	if lucia.key_pressed(lucia.K_a):
		lucia.output.output("Hey.")
	if lucia.key_pressed(lucia.K_q):
		break

lucia.quit()

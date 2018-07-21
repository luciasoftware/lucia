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

import sys, os, pygame, gettext

from openal import *

import lucia.globals as globals
from .audio.soundpool import *
from .audio.sound import *

from .resourcemanager import *

import appdirs, os

def init(appdev, appname, language="en"):
	globals.data_dir = appdirs.user_data_dir(appname, appdev, roaming=True)
	globals.temp_dir = os.path.join(appdirs.user_data_dir(appname, appdev, roaming=True), "/temp/")
	globals.screen = pygame.display.set_caption(appname)
	if os.path.isdir(globals.data_dir) == False:
		os.makedirs(globals.data_dir)
	if os.path.isdir(globals.temp_dir) == False:
		os.makedirs(globals.temp_dir)
	globals.screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
	pygame.mouse.set_visible(0)
	pygame.init()
	oalInit()
	oalSetStreamBufferCount(400)
	#translator = gettext.translation(appname, localedir='locale')
	#translator.install()

def quit():
	oalQuit()

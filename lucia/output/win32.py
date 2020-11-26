# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
from cytolk import tolk

from lucia.output.generic import GenericOutputDriver


class WindowsOutputDriver(GenericOutputDriver):
    def __init__(self):
        tolk.try_sapi(True)
        tolk.load()

    def output(self, message, interrupt=True):
        return tolk.output(message, interrupt)

    def speak(self, message, interrupt=True):
        return tolk.speak(message, interrupt)

    def braille(self, message):
        return tolk.braille(message)

    def is_speaking(self):
        return tolk.is_speaking()

# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
class GenericOutputDriver:
    def output(self, message):
        pass

    def speak(self, message):
        pass

    def braille(self, message):
        pass

    def is_speaking(self, message):
        pass

# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
from AppKit import NSSpeechSynthesizer  # type: ignore

from lucia.output.generic import GenericOutputDriver


class DarwinOutputDriver(GenericOutputDriver):
    def __init__(self):
        self._speech_driver = NSSpeechSynthesizer.alloc().init()

    def output(self, message, interrupt=True):
        return self.speak(message, interrupt)

    def speak(self, message, interrupt=True):
        if interrupt:
            self._speech_driver.startSpeakingString_(" ")
        self._speech_driver.startSpeakingString_(message)

    def is_speaking(self):
        return self._speech_driver.isSpeaking()

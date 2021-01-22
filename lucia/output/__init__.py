# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
import platform

from lucia.logger import logger
from lucia.exceptions import LuciaNotInitializedException

_driver = None


def init():
    global _driver
    if platform.system() == "Windows":
        from lucia.output.win32 import WindowsOutputDriver

        _driver = WindowsOutputDriver()
    if platform.system() == "Darwin":
        from lucia.output.darwin import DarwinOutputDriver

        _driver = DarwinOutputDriver()
    if platform.system() == "Linux":
        from lucia.output.linux import LinuxOutputDriver

        _driver = LinuxOutputDriver()
    logger.debug("Output driver set to {}.".format(_driver))
    logger.info("Output initialized.")


def quit() -> bool:
    global _driver
    if not _driver:
        return False
    _driver = None
    return True


def output(message: str, interrupt: bool = True) -> bool:
    """Output a message through speech and braille.

    Args:
        message (str): Message to output
        interrupt (bool, optional): Interrupt previous outputted message. Defaults
         to True:bool.

    Raises:
        LuciaNotInitializedException: Raised if called before lucia is initialized.

    Returns:
        bool: Returns True if the message was outputted, false otherwise.
    """
    global _driver
    if not _driver:
        raise LuciaNotInitializedException
    return _driver.output(message, interrupt)


def speak(message: str, interrupt: bool = True) -> bool:
    """Speak a message.

    Args:
        message (str): Message to output
        interrupt (bool, optional): Interrupt previous message. Defaults to True.

    Raises:
        LuciaNotInitializedException: Raised if called before lucia is initialized.

    Returns:
        bool: Returns True if the message was spoken, False otherwise.
    """
    global _driver
    if not _driver:
        raise LuciaNotInitializedException
    return _driver.speak(message, interrupt)


def braille(message: str) -> bool:
    """Braille a message.

    Args:
        message (str): Message to output

    Raises:
        LuciaNotInitializedException: Raised if called before lucia is initialized.

    Returns:
        bool: Returns True if the message was brailled, False otherwise.
    """
    global _driver
    if not _driver:
        raise LuciaNotInitializedException
    return _driver.braille(message)


def is_speaking() -> bool:
    """Check if the current output is still speaking.

    Raises:
        LuciaNotInitializedException: Raised if called before lucia is initialized.

    Returns:
        bool: True if the output is speaking, False otherwise.
    """
    global _driver
    if not _driver:
        raise LuciaNotInitializedException
    return _driver.is_speaking()

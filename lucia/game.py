# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
import atexit

import pygame

import lucia.output
from lucia.logger import logger


def init() -> None:
    """Initialize lucia and related modules."""
    logger.info("Initializing lucia.")
    pygame.init()
    lucia.output.init()
    atexit.register(quit)
    logger.info("Lucia initialized.")


def quit() -> None:
    """Quits lucia and relating modules, will be called automatically on exit."""
    logger.info("Shutting down lucia")
    pygame.quit()
    lucia.output.quit()
    logger.info("Lucia has been shut down.")

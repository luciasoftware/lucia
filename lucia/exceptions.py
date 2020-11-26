# Copyright LuciaSoftware 2019 - 2020
#
# Distributed under the Boost Software License, Version 1.0.
# (See accompanying file LICENSE or copy at
# https://www.boost.org/LICENSE_1_0.txt)
class LuciaException(Exception):
    """Generic lucia exception."""

    pass


class LuciaNotInitializedException(LuciaException):
    """Thrown when trying to use a module,
    class or function that requires lucia to be initialized."""

    pass

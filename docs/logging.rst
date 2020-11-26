.. _logging_setup:

Setting Up Logging
===================

Lucia logs errors and debug information via the :mod:`logging` python
module. It is strongly recommended that the logging module is
configured, as no errors or warnings will be output if it is not set up.
Configuration of the ``logging`` module can be as simple as::

    import logging

    logging.basicConfig(level=logging.INFO)

Placed at the start of the application. This will output the logs from
lucia as well as other libraries that uses the ``logging`` module
directly to the console.

The optional ``level`` argument specifies what level of events to log
out and can any of ``CRITICAL``, ``ERROR``, ``WARNING``, ``INFO``, and
``DEBUG`` and if not specified defaults to ``WARNING``.

For more information, check the documentation and tutorial of the logging module.

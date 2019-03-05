from accessible_output2.outputs.auto import *

output = Auto()
"""
Functions:
get_first_available_output() - autoselects the first available output.
speak(text, interrupt=False) - speaks some text.
silence() - Silence the current output if speaking.
braille(text, **options) - braills some output.
output(text, *args) - Both speak and braille some text.
is_active() - checks if the given output is active.
"""

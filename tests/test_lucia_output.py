import pytest

import lucia
from lucia.output.generic import GenericOutputDriver
from lucia.exceptions import LuciaNotInitializedException

def test_lucia_output_output():
    with pytest.raises(LuciaNotInitializedException):
        lucia.output.output("test")

def test_lucia_output_speak():
    with pytest.raises(LuciaNotInitializedException):
        lucia.output.speak("test")

def test_lucia_output_braille():
    with pytest.raises(LuciaNotInitializedException):
        lucia.output.braille("test")

def test_lucia_output_is_speaking():
    with pytest.raises(LuciaNotInitializedException):
        lucia.output.is_speaking()

def test_lucia_output_pre_init():
    assert lucia.output._driver is None

def test_lucia_output_init():
    lucia.output.init()
    assert lucia.output._driver is not None
    assert issubclass(type(lucia.output._driver), GenericOutputDriver)
    lucia.output.quit()

def test_lucia_output_post_init():
    assert lucia.output._driver is None


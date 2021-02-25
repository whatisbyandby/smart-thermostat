import pytest
from user_interface import UserInterface

def test_convert_f_to_c():
    assert UserInterface.convert_F_to_C(212) == 100
    assert UserInterface.convert_F_to_C(32) == 0
    assert UserInterface.convert_F_to_C(-40) == -40

def test_convert_c_to_f():
    assert UserInterface.convert_C_to_F(100) == 212
    assert UserInterface.convert_C_to_F(0) == 32
    assert UserInterface.convert_C_to_F(-40) == -40
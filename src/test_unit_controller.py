import pytest
from unit_controller import UnitController

def test_convert_f_to_c():
    assert UnitController.convert_f_to_c(212) == 100
    assert UnitController.convert_f_to_c(32) == 0
    assert UnitController.convert_f_to_c(-40) == -40

def test_convert_c_to_f():
    assert UnitController.convert_c_to_f(100) == 212
    assert UnitController.convert_c_to_f(0) == 32
    assert UnitController.convert_c_to_f(-40) == -40
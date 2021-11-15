import pytest

from montecarlodlgapp import MonteCarloAppDrop, MyDataDROP

given = pytest.mark.parametrize


def test_myApp_class():
    first = MonteCarloAppDrop("a", "a")
    second = MonteCarloAppDrop("a", "a")
    second.randomSeed = 100
    first.initialize()
    second.initialize()
    pi_1 = first.run()
    assert pi_1 != second.run()


def test_myData_class():
    assert MyDataDROP("a", "a").getIO() == "Hello from MyDataDROP"


def test_myData_dataURL():
    assert MyDataDROP("a", "a").dataURL == "Hello from the dataURL method"

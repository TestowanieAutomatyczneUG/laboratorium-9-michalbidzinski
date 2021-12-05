import unittest
from unittest.mock import *
from Car import Car
from CarImpl import CarImpl



class TestCar(unittest.TestCase):
    def test_no_fuel_needed(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = False
        carImpl = CarImpl(car)
        self.assertEqual("enough fuel", carImpl.need_fule())

    def test_fuel_needed(self):
        car = Car()
        car.needsFuel = Mock(name='needsFuel')
        car.needsFuel.return_value = True
        carImpl = CarImpl(car)
        self.assertEqual("need fuel", carImpl.need_fule())
    def test_engine_temperature_too_low(self):
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 60
        carImpl = CarImpl(car)
        self.assertEqual("temperature is too low", carImpl.engine_temperature())

    def test_engine_temperature_too_high(self):
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 110
        carImpl = CarImpl(car)
        self.assertEqual("temperature is too high", carImpl.engine_temperature())

    def test_engine_temperature_is_ok(self):
        car = Car()
        car.getEngineTemperature = Mock(name="getEngineTemperature")
        car.getEngineTemperature.return_value = 90
        carImpl = CarImpl(car)
        self.assertEqual("temperature is fine", carImpl.engine_temperature())

    def test_drive_to(self):
        car = Car()
        car.driveTo = Mock(name="driveTo")
        car.driveTo.return_value = "Warszawa"
        carImpl = CarImpl(car)
        self.assertEqual("Driving to Warszawa", carImpl.driving_to("Warszawa"))
    def test_drive_to_None(self):
        car = Car()
        car.driveTo = Mock(name="driveTo")
        car.driveTo.return_value = None
        carImpl = CarImpl(car)
        self.assertEqual("No destination", carImpl.driving_to(None))






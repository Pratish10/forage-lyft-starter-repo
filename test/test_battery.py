import unittest
import datetime

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2023, 5, 10)
        last_service_date = datetime.datetime(2020, 1, 5)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2023, 5, 10)
        last_service_date = datetime.datetime(2022, 1, 1)
        battery = NubbinBattery(last_service_date,current_date)
        self.assertFalse(battery.battery_should_be_serviced())

class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime.datetime(2023, 5, 10)
        last_service_date = datetime.datetime(2018, 1, 5)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertTrue(battery.battery_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        current_date = datetime.datetime(2023, 5, 10)
        last_service_date = datetime.datetime(2022, 1, 1)
        battery = SpindlerBattery(last_service_date,current_date)
        self.assertFalse(battery.battery_should_be_serviced())
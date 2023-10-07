import sys
import unittest
from datetime import date, datetime

# Import the methods and classes required for testing
from car_factory import CarFactory
from car import Car
from carComponents.battery import NubbinBattery, SpindlerBattery
from carComponents.engine import CapuletEngine, SternmanEngine, WilloughbyEngine



class TestCarCreation(unittest.TestCase):
    def testCalliope(self):
        calliope = CarFactory.create_calliope(self, datetime.today, datetime.today(), 100, 2000)
        
    def testGlissade(self):
        calliope = CarFactory.create_glissade(self, datetime.today, datetime.today(), 100, 2000)
        
    def testPalindrome(self):
        calliope = CarFactory.create_palindrome(self, datetime.today, datetime.today(), 100, 2000, False)
        
    def testRorschach(self):
        calliope = CarFactory.create_rorschach(self, datetime.today, datetime.today(), 100, 2000)
        
    def testThovex(self):
        calliope = CarFactory.create_thovex(self, datetime.today, datetime.today(), 100, 2000)


# # print(datetime.today())
# # format:   2023-10-06 12:28:17.470278


# python test_car.py



if __name__ == '__main__':
    unittest.main()
    





# # Old Tests
# class TestCalliope(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Calliope(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestGlissade(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 1)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Glissade(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestPalindrome(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = True

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         warning_light_is_on = False

#         car = Palindrome(last_service_date, warning_light_is_on)
#         self.assertFalse(car.needs_service())


# class TestRorschach(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60001
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 60000
#         last_service_mileage = 0

#         car = Rorschach(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())


# class TestThovex(unittest.TestCase):
#     def test_battery_should_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 5)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_battery_should_not_be_serviced(self):
#         today = datetime.today().date()
#         last_service_date = today.replace(year=today.year - 3)
#         current_mileage = 0
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

#     def test_engine_should_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30001
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertTrue(car.needs_service())

#     def test_engine_should_not_be_serviced(self):
#         last_service_date = datetime.today().date()
#         current_mileage = 30000
#         last_service_mileage = 0

#         car = Thovex(last_service_date, current_mileage, last_service_mileage)
#         self.assertFalse(car.needs_service())

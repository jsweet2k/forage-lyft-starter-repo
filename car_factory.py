from datetime import datetime
from car import Car
from carComponents.battery import NubbinBattery, SpindlerBattery
from carComponents.engine import CapuletEngine, SternmanEngine, WilloughbyEngine

class CarFactory:
    
    @staticmethod
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, datetime.today())
        calliope = Car(engine, battery)
        return calliope
    
    @staticmethod
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, datetime.today())
        glissade = Car(enigne, battery)
        return glissade
    
    @staticmethod
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage, warning_light_is_on):
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, datetime.today())
        palindrome = Car(engine, battery)
        return palindrome
    
    @staticmethod
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, datetime.today())
        rorschach = Car(engine, battery)
        return rorschach
    
    @staticmethod
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, datetime.today())
        thovex = Car(engine, battery)
        return thovex
    
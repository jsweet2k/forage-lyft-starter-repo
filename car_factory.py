from abc import ABC, abstractmethod
from carComponents import *

from car import Car

class CarFactory():
    
    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car
    
    def create_palindrome(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car
    
    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car
    
    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):
        return Car
    
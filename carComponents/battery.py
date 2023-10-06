from interfaces import IServiceable
from abc import ABC

class Battery(ABC, IServiceable):
    
    @abstractmethod
    def needs_service(self):
        pass

    
class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        pass 

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        pass 
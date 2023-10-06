from interfaces import IServiceable
from abc import ABC

class Tyres(ABC, IServiceable):
    
    @abstractmethod
    def needs_service(self):
        pass

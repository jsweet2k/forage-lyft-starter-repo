from interfaces.serviceable import IServiceable
from abc import ABC


class Tyres(ABC):

    def needs_service(self):
        pass
    
    
class OctoprimeTyres(Tyres):
    def __init__(self, tyresWearArray):
        super().__init__()
        self.tyresWearArray = tyresWearArray

    def needs_service(self):
        sumOfTyres = 0
        for tyre in self.tyresWearArray:
            sumOfTyres += tyre;
        if sumOfTyres >= 3:
            return True
        else:
            return False
    

class CarriganTyres(Tyres):
    def __init__(self, tyresWearArray):
        super().__init__()
        self.tyresWearArray = tyresWearArray
        
    def needs_service(self):
        sumOfTyres = 0
        for tyre in self.tyresWearArray:
            if tyre >= 0.9:
                return True
        return False

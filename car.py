from carComponents.engine import *
from carComponents.battery import *
from carComponents.tyres import *
from interfaces import IServiceable
from car_factory import CarFactory


class Car(CarFactory, IServiceable):
    
    def __init__(self, engine, tyres, battery):
        self.engine = engine
        self.tyres = tyres
        self.battery = battery
        

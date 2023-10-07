import unittest
from datetime import date, datetime

# Import the methods and classes required for testing
from car_factory import CarFactory
from car import Car
from carComponents.battery import NubbinBattery, SpindlerBattery
from carComponents.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from carComponents.tyres import OctoprimeTyres, CarriganTyres
from utils import increaseTyreWear



class TestCarCreation(unittest.TestCase):
    

    def testCalliopeBatteryServiceTrue(self): # Expected: Car needs Service
        calliope = CarFactory.create_calliope(self, datetime(2027,5,21,4), datetime.today(), 2001, 2000)

        print("\n-------------\n  Expected: Car needs Service \n")
        
        print("Does Battery need service: ", calliope.battery.needs_service())
        print("Does Engine need service: ", calliope.engine.needs_service())
        print("Does the car need servicing? : ", calliope.needs_service())
        self.assertTrue(calliope.needs_service())
        
    def testCalliopeBatteryServiceFalse(self): # Expected: Car doesnt Service
        calliope = CarFactory.create_calliope(self, datetime(2023,5,21,4), datetime.today(), 2001, 2000)

        print("\n-------------\n  Expected: Car doesnt need Service \n")
        
        print("Does Battery need service: ", calliope.battery.needs_service())
        print("Does Engine need service: ", calliope.engine.needs_service())
        print("Does the car need servicing? : ", calliope.needs_service())
        self.assertFalse(calliope.needs_service())
        
       
        
    def testPalindromeEngineServiceFalse(self): # Expected: Car doesnt need Service
        palindrome = CarFactory.create_palindrome(self, datetime(2025,7,15,1), datetime.today(), 100, 2000, False)
        
        print("\n-------------\n  Expected: Car doesnt need Service \n")
        
        print("Does Battery need service: ", palindrome.battery.needs_service())
        print("Does Engine need service: ", palindrome.engine.needs_service())
        print("Does the car need servicing? : ", palindrome.needs_service())
        self.assertFalse(palindrome.needs_service())
        
    def testPalindromeEngineServiceTrue(self): # Expected: Car does need Service
        palindrome = CarFactory.create_palindrome(self, datetime(2025,7,15,1), datetime.today(), 100, 2000, True)
        
        print("\n-------------\n  Expected: Car does need Service \n")
        
        print("Does Battery need service: ", palindrome.battery.needs_service())
        print("Does Engine need service: ", palindrome.engine.needs_service())
        print("Does the car need servicing? : ", palindrome.needs_service())
        self.assertTrue(palindrome.needs_service())
        
        
    def testRorschachBatteryServiceFalse(self): # Expected: Car doesnt need Service
        rorschach = CarFactory.create_rorschach(self, datetime(2022, 7 , 1, 3), datetime.today(), 100, 2000)
        
        
        print("\n-------------\n  Expected: Car doesnt need Service \n")
        
        print("Does Battery need service: ", rorschach.battery.needs_service())
        print("Does Engine need service: ", rorschach.engine.needs_service())
        print("Does the car need servicing? : ", rorschach.needs_service())
        self.assertFalse(rorschach.needs_service())
        

    def testRorschachBatteryServiceTrue(self): # Expected: Car does need Service
        rorschach = CarFactory.create_rorschach(self, datetime(2028, 7 , 1, 3), datetime.today(), 100, 2000)
        
        print("\n-------------\n  Expected: Car does need Service \n")
        
        print("Does Battery need service: ", rorschach.battery.needs_service())
        print("Does Engine need service: ", rorschach.engine.needs_service())
        print("Does the car need servicing? : ", rorschach.needs_service())
        self.assertTrue(rorschach.needs_service())
        
    def testThovexEngineServiceFalse(self): # Expected: Car doesnt need Service
        thovex = CarFactory.create_thovex(self, datetime(2022, 8, 3, 1), datetime.today(), 100, 2000)
        
        print("\n-------------\n  Expected: Car doesnt need Service \n")
        
        print("Does Battery need service: ", thovex.battery.needs_service())
        print("Does Engine need service: ", thovex.engine.needs_service())
        print("Does the car need servicing? : ", thovex.needs_service())
        self.assertFalse(thovex.needs_service())
        
    def testThovexEngineServiceTrue(self): # Expected: Car does need Service
        thovex = CarFactory.create_thovex(self, datetime(2022, 8, 3, 1), datetime.today(), 45000, 2000)
                
        print("\n-------------\n  Expected: Car does need Service \n")
        
        print("Does Battery need service: ", thovex.battery.needs_service())
        print("Does Engine need service: ", thovex.engine.needs_service())
        print("Does the car need servicing? : ", thovex.needs_service())
        self.assertTrue(thovex.needs_service())
        
    ## Tyres Test

    def testTyresArrayFunctionality(self): # Test the array increase functionality
        tyre = OctoprimeTyres([1,0.5,1,1])
        
        print("\n-------------\n Tyres Array Functionality Test")
        print("Pre Increase: ",tyre.tyresWearArray)
        
        tyre.tyresWearArray = increaseTyreWear(tyre.tyresWearArray, 1, 0.5)
        print("Post Increase: ", tyre.tyresWearArray) # Expected to increase array index 1 by 0.5

    def testOctoprimeTyresNeedsService(self):
        tyreThatDoesntNeedService = OctoprimeTyres([1,0.2,0.5,0.9])
        tyreThatDoesNeedService = OctoprimeTyres([1,1,0.5,0.6])
        
        print("\n-------------\n Ocotoprime Tyres Needs Service Test")
        print("Expected: False -> Tyre that doesnt need service: ", tyreThatDoesntNeedService.needs_service())
        print("Expected: True -> Tyre that does need service: ", tyreThatDoesNeedService.needs_service())
        
    def testCarriganTyresNeedsService(self):
        tyreThatDoesntNeedService = CarriganTyres([0.5,0.2,0.5,0.6])
        tyreThatDoesNeedService = CarriganTyres([0.4,0.1,0.5,0.9])
        
        print("\n-------------\n Carrigan Tyres Needs Service Test")
        print("Expected: False -> Tyre that doesnt need service: ", tyreThatDoesntNeedService.needs_service())
        print("Expected: True -> Tyre that does need service: ", tyreThatDoesNeedService.needs_service())





if __name__ == '__main__':
    unittest.main()
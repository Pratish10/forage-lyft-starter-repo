# + create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
# + create_glissade(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
# + create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool): Car
# + create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car
# + create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int): Car

#  	                Service criteria
# Capulet Engine	Once every 30,000 miles
# Willoughby Engine	Once every 60,000 miles
# Sternman Engine	Only when the warning indicator is on
# Spindler Battery	Once every 2 years
# Nubbin Battery	Once every 4 years

# Car	        Engine	            Battery
# Calliope	    Capulet Engine	    Spindler Battery
# Glissade	    Willoughby Engine	Spindler Battery
# Palindrome	Sternman Engine	    Spindler Battery
# Rorschach	    Willoughby Engine	Nubbin Batte
# Thovex	    Capulet Engine	    Nubbin Battery

from car_factory.car import Car

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class Car_Factory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_palindrome(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = SternmanEngine(current_mileage,last_service_mileage)
        battery = SpindlerBattery(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        car = Car(engine,battery)
        return car
    
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(current_mileage,last_service_mileage)
        battery = NubbinBattery(current_date,last_service_date)
        car = Car(engine,battery)
        return car
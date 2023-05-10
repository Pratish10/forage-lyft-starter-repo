from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self,tire_wear):
        self.tire_wear = tire_wear
        self.tire_service = 3

    def needs_service(self):
        return sum(self.tire_wear) >= self.tire_service
from battery.battery import Battery 
import datetime

class NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def battery_should_be_serviced(self):
        four_yrs = datetime.timedelta(days=365*4)
        diff = self.current_date - self.last_service_date
        if diff >= four_yrs:
            return True
        else:
            return False

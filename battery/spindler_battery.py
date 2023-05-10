from battery.battery import Battery 
import datetime

class SpindlerBattery(Battery):
    def __init__(self, last_service_date, current_date):
        super().__init__(last_service_date)
        self.current_date = current_date
        self.last_service_date = last_service_date

    def engine_should_be_serviced(self):
        two_yrs = datetime.timedelta(days=365*2)
        diff = self.current_date - self.last_service_date
        if diff >= two_yrs:
            return True
        else:
            return False
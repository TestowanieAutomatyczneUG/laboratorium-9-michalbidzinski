from Car import Car
class CarImpl():
    def __init__(self, car: Car):
        self.car = car
    def need_fule(self):
        if self.car.needsFuel():
            return "need fuel"
        else:
            return "enough fuel"
    def engine_temperature(self):
        if self.car.getEngineTemperature() < 80:
            return "temperature is too low"
        elif self.car.getEngineTemperature() > 100:
            return "temperature is too high"
        else:
            return "temperature is fine"
    def driving_to(self, destination):
        if self.car.driveTo(destination):
            return f"Driving to {destination}"
        else:
            return "No destination"
class Vehicle:
    DEFAULT_FUEL_CONSUMPTION: float = 1.25
    fuel_consumption: float
    fuel: float
    horse_power: int

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        if kilometers * self.fuel_consumption <= self.fuel:
            self.fuel -= kilometers * self.fuel_consumption

from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @property
    @abstractmethod
    def _AC_INCREASE(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def _REFUEL_EFFICIENCY(self):
        raise NotImplementedError

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self._AC_INCREASE):
            self.fuel_quantity -= distance * (self.fuel_consumption + self._AC_INCREASE)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self._REFUEL_EFFICIENCY


class Car(Vehicle):
    _AC_INCREASE = 0.9
    _REFUEL_EFFICIENCY = 1.0


class Truck(Vehicle):
    _AC_INCREASE = 1.6
    _REFUEL_EFFICIENCY = 0.95


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

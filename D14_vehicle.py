from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    AC_INCREASE = 0.9

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self.AC_INCREASE):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_INCREASE)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_INCREASE = 1.6
    REFUEL_EFFICIENCY = 0.95

    def drive(self, distance):
        if self.fuel_quantity >= distance * (self.fuel_consumption + self.AC_INCREASE):
            self.fuel_quantity -= distance * (self.fuel_consumption + self.AC_INCREASE)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * self.REFUEL_EFFICIENCY


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


import unittest
from D14_vehicle import *


class VehicleTest(unittest.TestCase):
    def setUp(self):
        self.car = Car(50, 10)
        self.truck = Truck(200, 20)

    def test_init(self):
        self.assertEqual(self.car.fuel_quantity, 50)
        self.assertEqual(self.car.fuel_consumption, 10)
        self.assertEqual(self.truck.fuel_quantity, 200)
        self.assertEqual(self.truck.fuel_consumption, 20)

    def test_drive_car_out_of_range(self):
        self.car.drive(1000)
        self.assertEqual(self.car.fuel_quantity, 50)

    def test_drive_car_in_range(self):
        self.car.drive(1)
        self.assertEqual(self.car.fuel_quantity, 50-1*(10+0.9))

    def test_car_refuel(self):
        self.car.refuel(9)
        self.assertEqual(self.car.fuel_quantity, 50+9)

    def test_drive_truck_out_of_range(self):
        self.truck.drive(1000)
        self.assertEqual(self.truck.fuel_quantity, 200)

    def test_drive_truck_in_range(self):
        self.truck.drive(1)
        self.assertEqual(self.truck.fuel_quantity, 200-1*(20+1.6))

    def test_truck_refuel(self):
        self.truck.refuel(9)
        self.assertEqual(self.truck.fuel_quantity, 200+9*.95)

if __name__ == '__main__':
    unittest.main()
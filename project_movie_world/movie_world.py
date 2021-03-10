from project_movie_world.customer import Customer
from project_movie_world.dvd import DVD
from typing import List


class MovieWorld:
    customers: List[Customer]
    dvds: List[DVD]

    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd = None
        customer = None
        for c in self.customers:
            if c.id == customer_id:
                customer = c
                break
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
                break

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        if dvd.is_rented:
            return f"DVD is already rented"
        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        dvd.is_rented = True
        customer.rented_dvds.append(dvd)
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int):
        customer = None
        dvd = None
        for c in self.customers:
            if c.id == customer_id:
                customer = c
                break
        for d in self.dvds:
            if d.id == dvd_id:
                dvd = d
                break
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = "\n".join([el.__repr__() for el in self.customers])
        result += "\n"
        result += "\n".join([el.__repr__() for el in self.dvds])
        return result

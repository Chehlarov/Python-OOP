from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.laptop import Laptop

from typing import List


class YoungCouple(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.calculate_expenses(*self.appliances)

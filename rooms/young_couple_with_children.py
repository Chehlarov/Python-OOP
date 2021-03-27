from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.laptop import Laptop
from ..people.child import Child

from typing import List


class YoungCoupleWithChildren(Room):

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children: Child):
        self.room_cost = 30
        self.children = list(children)
        members_count = 2 + len(self.children)
        self.appliances = []
        self.appliances.extend([TV(), Fridge(), Laptop()] * members_count)
        expenses = self.appliances + self.children
        self.calculate_expenses(*expenses)
        # self.expenses += sum([el.cost for el in self.children])
        super().__init__(family_name, salary_one + salary_two, members_count)

from .room import Room
from ..appliances.tv import TV
from ..appliances.fridge import Fridge
from ..appliances.stove import Stove

from typing import List


class OldCouple(Room):

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one+pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.calculate_expenses(*self.appliances)
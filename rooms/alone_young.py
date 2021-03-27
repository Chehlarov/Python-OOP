from .room import Room
from ..appliances.tv import TV
from typing import List


class AloneYoung(Room):

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances = [TV()]
        self.calculate_expenses(*self.appliances)

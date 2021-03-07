from math import sqrt


class Point:
    x: float
    y: float

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def set_x(self, new_x) -> None:
        self.x = new_x

    def set_y(self, ney_y) -> None:
        self.y = ney_y

    def distance(self, x, y) -> float:
        return sqrt((x - self.x) ** 2 + (y - self.y) ** 2)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))

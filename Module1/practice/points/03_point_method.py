import math
class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance_to(p1:Point, p2:Point) -> float:
       return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


# Дано две точки на координатной плоскости
point1 = Point(2, 4)
point2 = Point(5, -2)


print(f"Расстояние между точками = ",distance_to(p1,p2))

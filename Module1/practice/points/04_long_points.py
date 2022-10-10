import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def distance(p1:Point, p2:Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

max=0
for point in points:
    if distance(point,Point(0,0))>max:
        max=distance(point,Point(0,0))
        numP=point
print("Наиболее удаленная точка с координатами ", numP.x, ';', numP.y)


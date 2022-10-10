import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def distance(p1:Point, p2:Point) -> float:
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)

points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]
idx=1
leng=0
while idx< len(points):
    leng+=distance(points[idx-1],points[idx])
    idx=idx+1

print("Длина ломаной ", leng)


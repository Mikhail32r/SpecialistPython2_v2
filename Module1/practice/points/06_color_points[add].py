import math

class Point:
    def __init__(self, x, y,color):
        self.x = x
        self.y = y
        self.color = color


class Triangle:
    def __init__(self):
        self.listpoint = []
        self.ab = 0
        self.bc = 0
        self.ac = 0
        self.p = 0
        self.s = 0
    def add (self, p1):
        return self.listpoint.append(p1)
    def calc_s(self):
         self.ab = math.sqrt((self.listpoint[0].x - self.listpoint[1].x) ** 2 + (self.listpoint[0].y - self.listpoint[1].y) ** 2)
         self.bc = math.sqrt((self.listpoint[1].x - self.listpoint[2].x) ** 2 + (self.listpoint[1].y - self.listpoint[2].y) ** 2)
         self.ac = math.sqrt((self.listpoint[0].x - self.listpoint[2].x) ** 2 + (self.listpoint[0].y - self.listpoint[2].y) ** 2)
         self.p = (self.ab + self.bc + self.ac) / 2
         self.s = (self.p * (self.p - self.ac) * (self.p - self.bc)*(self.p - self.ab)) ** 0.5
         return self.s


points = [
        Point(2, 7, "red"),
        Point(12, 7, "green"),
        Point(5, -2, "red"),
        Point(4, 8, "green"),
        Point(10, -2, "green"),
        Point(-12, 0, "red")
    ]
tri_green = Triangle()
tri_red = Triangle()


for point in points:
   if point.color=="green":
       tri_green.add(point)
   if point.color == "red":
       tri_red.add(point)

print("Площадь треугольника(зеленый) = ", tri_green.calc_s())
print("Площадь треугольника(красный) = ", tri_red.calc_s())

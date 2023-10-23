from typing import Self, Type
from math import sqrt


class Point2D:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to_origin(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2))

    def distance_to_other(self, other: Type[Self]) -> float:

        return sqrt(((self.x - other.x) ** 2) + ((self.y - other.y)**2))

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"


point_a = Point2D(3, 5)
point_b = Point2D(1, 10)

# Calcul de la distance à l'origine
distance_origin = point_a.distance_to_origin()
print(f"Distance à l'origine : {distance_origin}")

# Calcul de la distance entre point_a et point_b
distance_to_point_b = point_a.distance_to_other(point_b)
print(f"Distance à point_b : {distance_to_point_b}")


class Point3D(Point2D):
    def __init__(self, x: float, y: float, z: float):
        Point2D.__init__(self, x, y)
        self.z = z

    def distance_to_origin(self) -> float:
        return sqrt((self.x ** 2) + (self.y ** 2) + (self.z**2))

    def distance_to_other(self, other: Type[Self]) -> float:

        return sqrt(((self.x - other.x) ** 2) + ((self.y - other.y)**2) + ((self.z - other.z)**2) )

    def __str__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"


point_a = Point3D(3, 5, 7)
point_b = Point3D(1, 10, 15)

distance_origin = point_a.distance_to_origin()
print(f"Distance à l'origine : {distance_origin}")

# Calcul de la distance entre point_a et point_b
distance_to_point_b = point_a.distance_to_other(point_b)
print(f"Distance à point_b : {distance_to_point_b}")
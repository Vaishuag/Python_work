import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def diameter(self):
        return 2 * self.radius

circle = Circle(7)
print("Circumference of Circle:", round(circle.circumference(), 2))  
print("Area of Circle:", round(circle.area(), 2))                  
print("Diameter of Circle:", circle.diameter())                    

import math

class Cone:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def slant_height(self):
        return math.sqrt(self.radius ** 2 + self.height ** 2)

    def surface_area(self):
        return math.pi * self.radius * (self.radius + self.slant_height())

    def volume(self):
        return (1 / 3) * math.pi * (self.radius ** 2) * self.height

cone = Cone(4, 9)
print("Slant Height of Cone:", round(cone.slant_height(), 2))  
print("Surface Area of Cone:", round(cone.surface_area(), 2))  
print("Volume of Cone:", round(cone.volume(), 2))              
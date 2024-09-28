from abc import ABC, abstractmethod
import math

def shape_info(arg):
    area = arg.area()
    perimeter = arg.perimeter()
    print(f"Area: {area}\nPerimeter: {perimeter}")


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius**2
        return area
    
    def perimeter(self):
        perimeter =2 * math.pi * self.radius
        return perimeter
    
class Rectangle(Shape):
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width * 2) + (self.height * 2)
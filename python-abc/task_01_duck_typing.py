from abc import ABC, abstractmethod
import math


def shape_info(arg):
    """
    Given an object 'arg' that inherits from the Shape class, this function calculates and prints
    its area and perimeter.
    """
    area = arg.area()
    perimeter = arg.perimeter()
    print(f"Area: {area}\nPerimeter: {perimeter}")


class Shape(ABC):
    """
    Abstract base class that defines the structure of a geometric shape.
    It requires that subclasses implement the 'area' and 'perimeter' methods.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """
    Represents a circle with a given radius. Inherits from the abstract Shape class.
    """

    def __init__(self, radius):
        """
        Initializes the Circle class with a radius.
        :param radius: Radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates and returns the area of the circle.
        :return: Area of the circle.
        """
        area = math.pi * self.radius**2
        return area

    def perimeter(self):
        """
        Calculates and returns the perimeter (circumference) of the circle.
        If the radius is negative, returns the perimeter as a positive value.
        :return: Perimeter of the circle.
        """
        if self.radius < 0:
            perimeter = (2 * math.pi * self.radius) * -1
        else:
            perimeter = 2 * math.pi * self.radius
        return perimeter


class Rectangle(Shape):
    """
    Represents a rectangle defined by its width and height. Inherits from the abstract Shape class.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle class with a width and height.
        :param width: Width of the rectangle.
        :param height: Height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        :return: Area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        :return: Perimeter of the rectangle.
        """
        return (self.width * 2) + (self.height * 2)

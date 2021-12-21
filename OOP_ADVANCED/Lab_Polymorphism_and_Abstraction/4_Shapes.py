import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        return

    @abstractmethod
    def calculate_perimeter(self):
        return


class Circle(Shape):

    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return (self.__radius ** 2) * math.pi

    def calculate_perimeter(self):
        return (self.__radius * math.pi) * 2


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__height

    def calculate_perimeter(self):
        return (self.__width + self.__height) * 2


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

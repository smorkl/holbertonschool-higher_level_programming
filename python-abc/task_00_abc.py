from abc import ABC, abstractmethod

"""
class of Animal
"""
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

"""
class Dog 
"""
class Dog(Animal):

    def sound(self):
        return "Bark"


"""
class Cat
"""
class Cat(Animal):

    def sound(self):
        return "Meow"

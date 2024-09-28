from abc import ABC, abstractmethod

class SwimMixin(ABC):
    @abstractmethod
    def swim(self):
        pass

class FlyMixin(ABC):
    @abstractmethod
    def fly(self):
        pass

class Dragon(SwimMixin, FlyMixin):
    def swim(self):
        print("The creature swims!")

    def fly(self):
        print("The creature flies!")

    def roar(self):
        print("The dragon roars!")
dragon = Dragon()
dragon.swim()  # Outputs: The creature swims!
dragon.fly()   # Outputs: The creature flies!
dragon.roar()  # Outputs: The dragon roars!
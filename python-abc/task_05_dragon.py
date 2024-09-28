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
        print("The dragon glides through the water!")

    def fly(self):
        print("The dragon soars through the sky!")

    def roar(self):
        print("The dragon roars!")

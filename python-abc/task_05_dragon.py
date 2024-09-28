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
    def roar(self):
        print("The dragon roars!")
from abc import ABC, abstractmethod


class Polygon(ABC):
    # abstract method
    def noofsides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


# Driver code
R = Triangle()
R.noofsides()
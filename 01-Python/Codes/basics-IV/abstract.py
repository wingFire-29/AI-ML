'''
Docstring for abstract
Abstraction means showing only essential details and hiding all the background work
datahiding means hiding of any type of data but absteraction means showeing neccessary
dertail and hiding complex details
These abstract classses are imported from abc module in python and function init are implemented in other classes

'''
from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod 
    def make_Sounds():
        pass

class Lion(Animal):
    def make_Sounds(self):
        print("ROAR")
        
lion=Lion()
lion.make_Sounds()

"""
When to use __str__ and __repr__?

Dunder methods start with double underscore ("___")

__str__ is used to give an easy to read representation of the class 
__repr__ unambiguous and meant for internal use or debug for developers and not made for end users

"""
class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage
    
    #added a dunder str method
    #when you print, this dunder method's string representation is printed on the screen
    #using the print() functions
    #Pythonic way to represent objects
    #demonstrate dunder "__str__" method
    def __str__(self):
        return "a {self.color} car".format(self = self)
    
    def __repr__(self):
        return "a repr {self.color} car".format(self = self)
    
#my_car = Car("red", 37281)

import datetime

today = datetime.date.today()

print(str(today))

"""Inheritance in python"""
# When a class derives from another class. The child class will inherit all the public and protected properties and methods from the parent class. In addition, it can have its own properties and methods,this is called as inheritance.
 
# Python Inheritance Syntax >
# class BaseClass:
#   Body of base class
# class DerivedClass(BaseClass):
#   Body of derived class
 
# Derived class inherits features from the base class where new features can be added to it. This results in re-usability of code.

# Types of inheritance > 

#> Single inheritance
#> Multiple inheritance
#> Multilevel inheritance
#> Hierarchical Inheritance
#> Hybrid Inheritance   


# Example >>
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The id of the Employee: {self.name} is {self.id}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")


p1 = Programmer("Mittesh", 123)
p1.showDetails()
p1.showLanguage()

p2 = Employee("Raju", 456)
p2.showDetails()
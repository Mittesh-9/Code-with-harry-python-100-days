class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Mittesh", 24)
print(p1.__dict__)

print(help(Person))
class Person:
    name = "Mittesh"
    occupation = "SDE"
    networth = "10000"
    def info(self):
        print(f"{self.name} is a {self.occupation}")        

# obj1 = Person()

a = Person()
b = Person()
c = Person()

a.name = "Mittesh"
a.occupation = "Bussinessman"

b.name = "Harry"
b.occupation = "Sr software developer"

c.name = "Nitika"
c.occupation = "HR"

# print(a.name, a.occupation)

# obj1.info()
a.info()
b.info()
c.info()
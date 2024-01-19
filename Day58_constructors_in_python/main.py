class Person:

    def __init__(self, name, occ):
        # print("Hey i am a person.")
        self.name = name
        self.occ = occ
        # self.info() # Learn more about this like how a function is being called before it is getting defined.

    def info(self):
        print(f"{self.name} is an {self.occ}")

a = Person("mittesh", "sde")
b = Person("niyati", "hr")

a.info()
b.info()

# print(a.name)
# a.name = "niyati"
# a.occ = "businesswoman"

# a.info()
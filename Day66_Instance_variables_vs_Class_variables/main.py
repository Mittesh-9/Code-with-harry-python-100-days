class Employee:
    companyName = "Google" # Class associated variables >> kuch cheeze generic hoti hai to unke liye directly class variables banaye jaate hai jaise yaha company name
    noOfEmployees = 0
    def __init__(self, name):
        self.name = name # Instance associated variables
        self.raise_amount = 0.02
        Employee.noOfEmployees += 1 # Iska matlab jaise jaise employees add hote hai waise waise noOfEmployees badhte jaege

    def showDetails(self):
        print(f"The name of the employee is {self.name} and the raise amount in {self.noOfEmployees} sized company {self.companyName} is {self.raise_amount}")

emp1 = Employee("Mittesh")
emp1.raise_amount = 0.5 # This can be changed like this because this is associated to the instance
emp1.companyName = "Google India" # iss case me output ke waqt (as a instance variable tha) toh kyuki instance variable maujud tha isiliye instance varible show hua - agar nahi hota toh tab class variable ke liye khoj ki jaati aur jab class variable mil jaata toh wo use le liye jaata tha
emp1.showDetails()
Employee.companyName = "Nokia"
print(Employee.companyName)

# Employee.showDetails(emp1) < same as >> emp1 = Employee("Mittesh") emp1.showDetails()

emp2 = Employee("Harry")
Employee.companyName = "JD Fincorp"
emp2.showDetails()
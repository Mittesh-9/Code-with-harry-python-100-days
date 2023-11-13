# You generally import modules as
import math

# Or you can import a function from the module as
from math import sqrt, pi

result = sqrt(4) * pi
print(result)

# If you want to import all the functions and variables of a module. (Not a recommended approachas it can lead to confusion and make it harder to understand where specific functions and variables are coming from.)
from math import *

# You can also give a name as of your choice to the module by using 'as' keyword
import pandas as pd
import math as m
from math import sqrt as sr

# You can use the inbuilt python function - dir() function, to view the names of all the functions and variables defined in a module
import math
print(dir(math))


from mittesh import welcome, mittesh
welcome()
print(mittesh)
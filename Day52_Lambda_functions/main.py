# def double(x):
#     return x * 2

double = lambda x : x * 2

# print(double(2))

def appl(func, value):
    return 5 + func(value)

# print(appl(double, 2)) # output >> 9

print(appl(lambda x : x * 2, 2))
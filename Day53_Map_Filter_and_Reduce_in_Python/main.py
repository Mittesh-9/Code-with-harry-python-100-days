# MAP

# def cube(x):
#     return x * x * x

lis = [1,2,3,4,5,6,7,8,9,10]

# new_lis = list(cube, lis))
new_lis = list(map(lambda x: x*x*x, lis))

print(new_lis)

# FILTER

# def filter_function(a):
#     return a > 4

# newnewl = list(filter(filter_function, lis))
newnewl = list(filter(lambda x : x > 4, lis))

print(newnewl)

# REDUCE

from functools import reduce

lis2 = [1,2,3,4,5]

# calculate the sum of numbers using the reduce function
sum = reduce(lambda x, y : x + y, lis2)

print(sum)
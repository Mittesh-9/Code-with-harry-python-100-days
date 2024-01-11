
a = 4
b = "4"

print(a is b) # exact location of object in memory >> output False
print(a == b) # value >> output False

a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(a is b) # exact location of object in memory >> output False
print(a == b) # value >> output True
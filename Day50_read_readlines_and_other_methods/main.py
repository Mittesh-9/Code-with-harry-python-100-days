# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open("marks.txt", "r")

# i = 0
# while True:
#     i = i + 1
#     line = f.readline()
#     m1 = int(line.split(",")[0])
#     m2 = int(line.split(",")[1])
#     m3 = int(line.split(",")[2])

#     print(f"Marks of student {i} in Maths is {m1/100*100}%")
#     print(f"Marks of student {i} in Science is {m2/100*100}%")
#     print(f"Marks of student {i} in Social science is {m3/100*100}%")

#     if not line:
#         break
#         print(line)

# f = open('myfile2.txt', 'w')
# lines = ['line 1\n', 'line 2\n', 'line 3\n', 'line 4\n', 'line 5\n']
# f.writelines(lines)
# f.close()

f = open('myfile3.txt', 'w')

lines = ["line1","line2","line3","line4","line5"]
for line in lines:
    f.write(line + "\n")
f.close()
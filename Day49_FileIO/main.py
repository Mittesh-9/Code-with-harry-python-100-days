# READING A FILE

# f = open("Day49_FileIO/myfile.txt", "r")
# content = f.read()
# print(content)
# f.close()

# WRITING A FILE

# f = open("Day49_FileIO/myfile2.txt", "w")
# f.write("Hello world !")
# f.close()

# APPENDING TO A FILE

# f = open("Day49_FileIO/myfile2.txt", "a")
# f.write("Appended > Hello world !")
# f.close()

# The 'With' statement
with open("Day49_FileIO/myfile2.txt", "a") as f:
    f.write("Hello i am using with statement")
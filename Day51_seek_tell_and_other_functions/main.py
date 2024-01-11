''' seek() function >> '''

with open("file.txt", "r") as f:
    # print(type(f))

    # move to the 10th byte in the file
    f.seek(10)

    # read the next 5 bytes
    data = f.read(5)

    print(data)


''' tell() function >> '''

with open("file2.txt", "r") as f:
    
    # read the first 10 bytes
    data = f.read(10)

    # save the current position
    current_position = f.tell()

    # seek to the saved position
    f.seek(current_position)

''' truncate() function >> '''

with open("sample.txt", "w") as f:
    f.write("Hello, World!")
    f.truncate(5)

with open("sample.txt", "r") as f:
    print(f.read())
# Write a program to clear the clutter inside a folder on your computer. You should use os module to rename all the png images from 1.png all the way till n.png where n is the number of png files in that folder. Do the same for other file formats. For example:

# sfdsf.png --> 1.png
# vfsf.png --> 2.png
# this.png --> 3.png
# design.png --> 4.png
# name.png --> 5.png

import os

# getting a list of files in the folder
file_list = os.listdir("/home/mittesh/Code-with-harry-python-100-days/Day68_Exercise_7_Clear_the_clutter/files")

def clear_the_clutter():
    number = 0
    for file in file_list:
        if file.endswith(".png"):
            number += 1
            os.rename(f"/home/mittesh/Code-with-harry-python-100-days/Day68_Exercise_7_Clear_the_clutter/files/{file}", f"/home/mittesh/Code-with-harry-python-100-days/Day68_Exercise_7_Clear_the_clutter/files/{number}.png")

clear_the_clutter()
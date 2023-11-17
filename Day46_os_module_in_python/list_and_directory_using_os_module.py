import os

print(os.getcwd()) # This prints the current directory you are in
# os.chdir("/Users") > This function changes your directory

folders = os.listdir("Day46_os_module_in_python/Data")
print(folders) # This prints folders randomly (not in a sequence)

for folder in folders:
    print(folder)
    print(os.listdir(f"Day46_os_module_in_python/Data/{folder}"))
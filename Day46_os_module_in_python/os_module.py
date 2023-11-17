import os


if (not os.path.exists("Day46_os_module_in_python/Data")):
    os.mkdir("Day46_os_module_in_python/Data")

for i in range(0, 10):
    os.mkdir(f"Day46_os_module_in_python/Data/Day{i + 1}")
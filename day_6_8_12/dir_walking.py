import os

print(os.path.abspath("../main.py"))
# C:\Users\Administrator\PycharmProjects\bootcamp16_11_2024\main.py

for root, dirs, files in os.walk("../.."):
    abs_root = os.path.abspath(root)
    # print(abs_root)
    if dirs:
        print("Directories")
        for dir_ in dirs:
            print(dir_)

    if files:
        print('Files')
        for filename in files:
            print(filename)

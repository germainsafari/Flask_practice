"""
import os
path = "C:\\Users\\safarig\\Desktop\\test.txt"
if os.path.exists(path):
    print("location exists")
else:
    print("location doesn't exist")
"""
with open("C:\\Users\\safarig\\Desktop\\test.txt") as file:
    print(file.read())

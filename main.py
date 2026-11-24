from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*')) 
    for i, items in enumerate(items): 
        print(f"{i+1} : {items} ")

print("press 1 for creating a file")
print("press 2 for reading a file")
print("press 3 for updating a file")
print("press 4 for deletion a file")

check = int(input("please tell your response :- "))

if check == 1;
    createFile()


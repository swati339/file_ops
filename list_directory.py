import os

print(f"Current Working Directory: {os.getcwd()}")

directory_path =  'C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project'

with os.scandir(directory_path) as entries:
    for entry in entries:
        print(entry.name)

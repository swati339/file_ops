import os

# Define the root directory
root_dir = 'C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project'

# Traverse the directory tree
for dirpath, dirnames, filenames in os.walk(root_dir):
    print(f"Directory: {dirpath}")
    for dirname in dirnames:
        print(f"  Subdirectory: {dirname}")
    for filename in filenames:
        print(f"  File: {filename}")

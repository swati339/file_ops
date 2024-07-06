import os
from pathlib import Path

# Define the directory path for both methods
dir_path_os = 'C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project'
dir_path_pathlib = Path('C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project')

# Create directory using os.mkdir() and os.makedirs()
try:
    os.mkdir(dir_path_os)
    print(f"Directory '{dir_path_os}' created using os.mkdir()")
except FileExistsError:
    print(f"Directory '{dir_path_os}' already exists")

os.makedirs(dir_path_os, exist_ok=True)
print(f"Directories '{dir_path_os}' created using os.makedirs()")

# Create directory using pathlib.Path.mkdir()
dir_path_pathlib.mkdir(parents=True, exist_ok=True)
print(f"Directory '{dir_path_pathlib}' created using pathlib.Path.mkdir()")

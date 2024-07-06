import os
import glob
import fnmatch

# Define the directory path and pattern
directory_path = 'C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project'
pattern = '*.txt'

# Using glob module
print("Using glob module:")
glob_pattern = os.path.join(directory_path, pattern)
matching_files_glob = glob.glob(glob_pattern)
for file in matching_files_glob:
    print(file)

print("\nUsing fnmatch module:")
# Using fnmatch module
matching_files_fnmatch = fnmatch.filter(os.listdir(directory_path), pattern)
for file in matching_files_fnmatch:
    print(file)

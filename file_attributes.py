from pathlib import Path
import time 

# Define the file path
file_path = Path('C:/Users/Dell Inspiron 7306/OneDrive/Desktop/my_project')

# Get file attributes
file_size = file_path.stat().st_size
last_modified = file_path.stat().st_mtime
last_accessed = file_path.stat().st_atime
creation_time = file_path.stat().st_ctime

# Print file attributes
print(f"File Size: {file_size} bytes")
print(f"Last Modified: {time.ctime(last_modified)}")
print(f"Last Accessed: {time.ctime(last_accessed)}")
print(f"Creation Time: {time.ctime(creation_time)}")

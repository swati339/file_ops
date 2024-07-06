
filename = 'data.txt'

# Open the file using with open() pattern
with open(filename, 'r') as file:
    # Read the entire content of the file
    data = file.read()
    
    # Print the read data
    print("File content:")
    print(data)

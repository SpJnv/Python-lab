# Open the file in read mode
file = open("ABC.txt", 'r')

# Read and print each line from the file
for line in file:
    print(line, end='')  # end='' prevents adding extra newline

# Close the file after reading
file.close()

#Output

"""
Hello Shivam pal.
Welcome to Anudip Foundation.
We provide skill development training for the underprivileged people & guarantee placement.
"""

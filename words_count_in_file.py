# Initialize a variable to keep track of the total word count
total_words = 0

# Open the file in read mode
file = open("ABC.txt", 'r')

# Read each line from the file
for line in file:
    # Split the line into words and update the total word count
    words = line.split()
    total_words += len(words)

# Close the file after reading
file.close()

# Display the total word count
print(f"Total number of words in ABC.txt: {total_words}")


#Output

"""
Total number of words in ABC.txt: 19

"""

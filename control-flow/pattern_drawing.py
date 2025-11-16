
# Ask the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Start with the first row
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks across the row
    for i in range(size):
        print("*", end="")
    
    # Move to the next line after each row
    print()
    
    # Go to the next row
    row += 1

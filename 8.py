# Function to print the times table
def print_times_table(number):
    if number < 0:
        # If the number is negative, print the table backwards
        number = abs(number)  # Get the absolute value for calculations
        for i in range(12, -1, -1):  # Loop from 12 down to 0
            print(f"{number} times {i} = {number * i}")
    else:
        # If the number is positive, print the table normally
        for i in range(0, 13):  # Loop from 0 to 12
            print(f"{number} times {i} = {number * i}")

# Get user input
user_input = int(input("Enter the number for the times table: "))
print_times_table(user_input)
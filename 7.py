def times_table():
    # Ask the user to enter a number between 0 and 12
    number = int(input("Enter a number between 0 and 12 to see its times table: "))
    
    # Check if the number is within the valid range
    if 0 <= number <= 12:
        print(f"Times Table for {number}:")
        for i in range(1, 13):
            print(f"{number} x {i} = {number * i}")
    else:
        print("Please enter a valid number between 0 and 12.")

# Call the function to execute the program
times_table()
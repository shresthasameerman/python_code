def distribute_sweets():
    # Input: number of sweets and number of pupils
    try:
        total_sweets = int(input("Enter the total number of sweets: "))
        number_of_pupils = int(input("Enter the number of pupils: "))
        
        # Check if the number of pupils is greater than 0 to avoid division by zero
        if number_of_pupils <= 0:
            print("The number of pupils must be greater than zero.")
            return
        
        # Calculate sweets per pupil and sweets left over
        sweets_per_pupil = total_sweets // number_of_pupils
        sweets_left_over = total_sweets % number_of_pupils
        
        # Output the results
        print(f"Each pupil will receive: {sweets_per_pupil} sweets.")
        print(f"Sweets left over: {sweets_left_over} sweets.")
    
    except ValueError:
        print("Please enter valid integers for sweets and pupils.")

# Run the function
distribute_sweets()
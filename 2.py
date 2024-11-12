def set_password():
    # Prompt the user for a new password
    password1 = input("Please enter a new password: ")
    # Prompt the user to confirm the password
    password2 = input("Please re-enter the password to confirm: ")
    
    # Check if the passwords match
    if password1 == password2:
        print("Password Set")
    else:
        print("Error: Passwords do not match. Please try again.")

# Run the password setting function
set_password()
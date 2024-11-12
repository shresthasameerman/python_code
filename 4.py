def is_valid_password(password):
    # Check if the password is alphanumeric
    return password.isalnum()

# Initialize a counter for bad passwords
bad_password_count = 0

# Allow user to enter passwords
while True:
    password = input("Enter a password (or type 'exit' to quit): ")
    
    if password.lower() == 'exit':
        break  # Exit the loop if the user types 'exit'
    
    if not is_valid_password(password):
        print(f"'{password}' is a bad password.")
        bad_password_count += 1
    else:
        print(f"'{password}' is a valid password.")

print(f"Total bad passwords: {bad_password_count}")
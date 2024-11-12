def is_valid_password(password):
    # Check password length
    if len(password) < 8:
        print("Password must be at least 8 characters long.")
        return False
    
    # Check for at least one uppercase letter
    if not any(char.isupper() for char in password):
        print("Password must contain at least one uppercase letter.")
        return False
    
    # Check for at least one lowercase letter
    if not any(char.islower() for char in password):
        print("Password must contain at least one lowercase letter.")
        return False
    
    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        print("Password must contain at least one digit.")
        return False
    
    # Check for at least one special character
    special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/"
    if not any(char in special_characters for char in password):
        print("Password must contain at least one special character.")
        return False
    
    return True

def main():
    while True:
        password = input("Please enter a password: ")
        if is_valid_password(password):
            print("Password set successfully!")
            break

if __name__ == "__main__":
    main()
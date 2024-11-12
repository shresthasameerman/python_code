def is_valid_password(password):
    # Check if the password length is between 8 and 12 characters
    if len(password) < 8 or len(password) > 12:
        return False
    
    # Check if the password contains at least one letter and one digit
    has_letter = any(char.isalpha() for char in password)
    has_digit = any(char.isdigit() for char in password)

    return has_letter and has_digit

def main():
    password = input("Enter your password: ")
    
    if is_valid_password(password):
        print("Your password is valid.")
    else:
        print("Your password must be between 8 and 12 characters long and contain at least one letter and one digit.")

if __name__ == "__main__":
    main()
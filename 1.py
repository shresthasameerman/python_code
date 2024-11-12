# Greeting program
name = input("Please enter your name: ")

if name.strip() == "":
    print("Hello, Stranger!")
else:
    print(f"Hello, {name}!")
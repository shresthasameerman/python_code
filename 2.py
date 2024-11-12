# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Prompt the user for temperature in Celsius
celsius_input = float(input("Enter a temperature in Celsius: "))

# Calculate the corresponding temperature in Fahrenheit
fahrenheit_output = celsius_to_fahrenheit(celsius_input)

# Display the result
print(f"{celsius_input}C is equivalent to {fahrenheit_output}F.")
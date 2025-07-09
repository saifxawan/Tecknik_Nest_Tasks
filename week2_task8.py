#  Temperature converter
# Celsius to Fahrenheit
try:
    celsius = float(input(" Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f" {celsius}°C is equal to {fahrenheit:.2f}°F")
except ValueError:
    print("❌ Please enter a valid number for Celsius.")

# Fahrenheit to Celsius
try:
    fahrenheit_input = float(input("\n Enter temperature in Fahrenheit: "))
    celsius_converted = (fahrenheit_input - 32) * 5/9
    print(f" {fahrenheit_input}°F is equal to {celsius_converted:.2f}°C")
except ValueError:
    print("❌ Please enter a valid number for Fahrenheit.")

user_input = input("Enter any value: ")

# Try guessing and converting the type
try:
    value = int(user_input)
    print("You entered an integer!")
except ValueError:
    try:
        value = float(user_input)
        print("You entered a float!")
    except ValueError:
        print("You entered a string!")

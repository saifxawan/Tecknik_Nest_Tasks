import math
try:
    radius_input = float(input("Tell me the radius of your circle: "))
    area = math.pi * math.pow(radius_input, 2)
    circumference = 2 * math.pi * radius_input
    sqrt_area = math.sqrt(area)
    print(f"The area of your circle is: {area:.2f}")
    print(f"The circumference of your circle is: {circumference:.2f}")
    print(f"And the square root of that area is: {sqrt_area:.2f}")
except ValueError:
    print("Hold on, that wasn't a valid number for the radius. Please enter a numerical value.")
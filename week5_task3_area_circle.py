import math
def calculate_area(circle_radius):
    area = math.pi * (circle_radius ** 2)
    return area
test_radius = 5.0
calculated_area = calculate_area(test_radius)
print(f"For a circle with radius {test_radius}, the area is: {calculated_area:.2f}")
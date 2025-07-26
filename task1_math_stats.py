# Task 1: Use math & statistics libraries to get square roots and average
import math
import statistics

numbers = [4, 9, 16, 25]
square_roots = [math.sqrt(n) for n in numbers]
average = statistics.mean(numbers)

print("Square Roots:", square_roots)
print("Average:", average)

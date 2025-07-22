def is_even_or_odd(number_to_check):
    if number_to_check % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(f"Is 7 even or odd? My function says: {is_even_or_odd(7)}")
print(f"How about 12? My function says: {is_even_or_odd(12)}")
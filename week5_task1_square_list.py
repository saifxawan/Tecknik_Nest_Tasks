def square_numbers(list_of_nums):
    squared_results = []
    for num in list_of_nums:
        squared_results.append(num ** 2)
    return squared_results
my_number_list = [10, 2, 8, 4, 6]
transformed_list = square_numbers(my_number_list)
print(f"My original numbers were: {my_number_list}")
print(f"After squaring them, I got: {transformed_list}")
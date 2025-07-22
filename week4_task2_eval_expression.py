expression_str = input("Enter a Python expression for me to calculate (e.g., '2 + 3 * 4'): ")
try:
    exec(f"print('The result of your expression is:', {expression_str})")
except Exception as e:
    print(f"Something went wrong while trying to evaluate your expression: {e}")
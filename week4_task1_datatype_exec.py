user_value = input("Hey there, could you type something in for me? Anything at all: ")
print(f"You know, Python sees that as a: {type(user_value)}")

code_to_run = input("Alright, now give me a line of Python code to execute (like: print('Hello, world!')): ")
try:
    exec(code_to_run)
except Exception as e:
    print(f"Oops! Looks like there was an error trying to run that code: {e}")
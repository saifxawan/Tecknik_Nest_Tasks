my_global_counter = 0
print(f"At the very beginning, my_global_counter is: {my_global_counter}")
def change_counter():
    global my_global_counter
    my_global_counter += 1
    print(f"Inside the function call, my_global_counter is now: {my_global_counter}")
change_counter()
change_counter()
print(f"After calling the function a couple of times, my_global_counter is finally: {my_global_counter}")
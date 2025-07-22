import random
import string
def generate_random_password(length=8):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password_list = [random.choice(all_characters) for _ in range(length)]
    return "".join(password_list)
my_new_password = generate_random_password(8)
print(f"Here's a randomly generated 8-character password for you: {my_new_password}")
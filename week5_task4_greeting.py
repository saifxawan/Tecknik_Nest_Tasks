def greet_user(user_name, user_age):
    greeting_message = f"Hello {user_name}, you are {user_age} years old."
    return greeting_message
person_name = "Saif"
person_age = 20
my_greeting = greet_user(person_name, person_age)
print(my_greeting)
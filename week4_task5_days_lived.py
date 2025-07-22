from datetime import datetime
try:
    birth_date_str_input = input("Please enter your birth date in YYYY-MM-DD format (e.g., 1990-05-15): ")
    birth_date_obj = datetime.strptime(birth_date_str_input, "%Y-%m-%d")
    current_time_obj = datetime.now()
    age_in_years = current_time_obj.year - birth_date_obj.year
    if (current_time_obj.month, current_time_obj.day) < (birth_date_obj.month, birth_date_obj.day):
        age_in_years -= 1
    total_days_lived = (current_time_obj - birth_date_obj).days
    print(f"Based on your input, you are {age_in_years} years old.")
    print(f"And you have been alive for approximately {total_days_lived} days!")
except ValueError:
    print("Oops! That date format seems incorrect. Please make sure it's YYYY-MM-DD.")
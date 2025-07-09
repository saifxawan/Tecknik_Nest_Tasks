# Voting eligibility

current_year = 2025
birth_year = int(input("Enter your birth year: "))

# Calculate age
age = current_year - birth_year
print(f"\nYou are {age} years old.")

# Check voting eligibility
if age >= 18:
    print("✅ You are eligible to vote.")
else:
    print("❌ You are not eligible to vote yet.")

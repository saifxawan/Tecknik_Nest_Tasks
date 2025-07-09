income = float(input("Enter monthly income: "))
expenses = float(input("Enter monthly expenses: "))

savings = income - expenses

if savings > 10000:
    status = "Saving Well"
elif savings >= 5000:
    status = "Average"
else:
    status = "Try to Save"

print("Your monthly savings:", savings)
print("Status:", status)

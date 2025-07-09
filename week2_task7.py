
try:
    print(" Enter marks out of 100 for each subject:")
    sub1 = int(input("Subject 1: "))
    sub2 = int(input("Subject 2: "))
    sub3 = int(input("Subject 3: "))
    sub4 = int(input("Subject 4: "))
    sub5 = int(input("Subject 5: "))

    # Calculate total and percentage
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = (total / 500) * 100

    # Determine grade
    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    else:
        grade = "Fail"

    # Output
    print(f"\n Total Marks: {total}/500")
    print(f" Percentage: {percentage:.2f}%")
    print(f" Grade: {grade}")

except ValueError:
    print("❌ Invalid input! Please enter numbers only.")

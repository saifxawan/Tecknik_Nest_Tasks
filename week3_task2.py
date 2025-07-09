sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

if percentage >= 85:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)

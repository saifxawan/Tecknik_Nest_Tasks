attendance = float(input("Enter attendance percentage: "))
marks = float(input("Enter final marks: "))

if attendance >= 75 and marks >= 50:
    print("Promoted")
else:
    print("Not Promoted")

# Ask the user for a grade percentage and display the corresponding letter grade (A, B, C, D, F).

grade = float(input("Enter a grade percentage: "))
if grade >= 90:
    print("Grade: A")
elif grade >= 80:
    print("Grade: B")
elif grade >= 70:
    print("Grade: C")
elif grade >= 60:
    print("Grade: D")
else:
    print("Grade: F")
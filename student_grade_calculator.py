print("Student Grade Calculator")

name = input("Enter the student's name: ")

grade1 = float(input("Enter first grade: "))
grade2 = float(input("Enter second grade: "))
grade3 = float(input("Enter third grade: "))

average = (grade1 + grade2 + grade3) / 3

print("Average grade:", average)

if average >= 3.0:
    print(name, "passed the course.")
else:
    print(name, "did not pass the course.")

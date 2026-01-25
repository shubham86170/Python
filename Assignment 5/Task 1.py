# Dictionary for student marks
student_marks = {
    "Alice": 85,
    "Bikas": 90,
    "Nitish": 78,
    "Deep": 92
}

# take user for student name
name = input("Enter the student's name: ")

# Check and display the result
if name in student_marks:
    print(f"{name}'s marks: {student_marks[name]}")
else:
    print("Student not found.")
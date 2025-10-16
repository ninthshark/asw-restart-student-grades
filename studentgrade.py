
user_input = input("How many students are there: ")

try:
    num_of_students = int(user_input)
except ValueError:
    print("Not valid number")

students = []

for student in range(num_of_students):
    student_record = {}
    name = input(f"Enter student {student + 1} name: ")
    student_record["name"] = name

    students.append(student_record)

    #adding subjects
    maths = int(input("What is the student's Maths mark? "))
    english = int(input("What is the student's English mark? "))
    history = int(input("What is the student's History mark? "))

    subjects = {}
    subjects["maths"] = maths
    subjects["english"] = english
    subjects["history"] = history

    student_record["subjects"] = subjects

    print("-" * 20)


print("{:<10} {:<10} {:<10} {:<10}".format("Name", "Maths", "English", "History"))

for _ in range(num_of_students):
    print 


# print(students)


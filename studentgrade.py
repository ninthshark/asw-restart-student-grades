def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# determine the column widht based on the lenght of a subject    
def spaces(subject):
    size = len(subject) + 3
    if size < 10:
        size = 10
    return size

def display_student_records(students):
    for student in students:
        total_mark = 0
        average_mark = 0
        max_col_width = 0
        print(f"Name: {student["name"]}")

        print(f"{"Subject":<15}", end="")
        for subject in student["subjects"]:
            col_width = spaces(subject)
            max_col_width = max(col_width, max_col_width)
            print(f"{subject:<{max_col_width}}", end="")
             
        print()

        print(f"{"Mark":<15}", end="")
        for value in student["subjects"].values():
            print(f"{value:<{max_col_width}}", end="")
        print()

        print(f"{"Grade":<15}", end="")
        for mark in student["subjects"].values():
            total_mark += mark
            print(f"{calculate_grade(mark):<{max_col_width}}", end="")
        print()

        print(f"{"Total Mark:":<15}", end="")
        print(f"{total_mark:<10}")

        print(f"{"Average Mark:":<15}", end="")
        print(f"{int(total_mark/len(students)):<10}")
        print("-" * 50)


user_input = input("How many students are there: ")

try:
    num_of_students = int(user_input)
except ValueError:
    print("Not valid number")

students = []

for student in range(num_of_students):
    student_record = {}
    name = input(f"Enter student {student + 1}'s name: ")
    student_record["name"] = name

    students.append(student_record)

    subjects = {}
    for _ in range(3):
        subject = input(f"What is subject {_ + 1}? ")
        mark = int(input(f"What is the student's {subject} mark? "))
        subjects[subject] = mark

    student_record["subjects"] = subjects
    print("-" * 40)

display_student_records(students)


# print(students)
# Test data
# students = [{'name': 'Jack Mah', 'subjects': {'English': 67, 'Maths': 78, 'History': 59}}, {'name': 'Sandy Wang', 'subjects': {'English': 78, 'Literature': 89, 'Chemistry': 92}}, {'name': 'Elong Meng', 'subjects': {'Computer Science': 92, 'Marketing': 97, 'Philosophy': 85}}]




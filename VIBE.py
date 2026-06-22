# Keisha Anderson
# CIS261
# WK10 VIBE Coding
# Student Grade Calculator

import os

DATA_FILE = "student_grades.txt"

def calculate_average(test1, test2, test3):
    return (test1 + test2 + test3) / 3

def determine_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def load_students_from_file():
    students = []

    if not os.path.exists(DATA_FILE):
        return students

    try:
        with open(DATA_FILE, "r") as file:
            for line in file:
                line = line.strip()

                if line == "":
                    continue

                parts = line.split("|")

                if len(parts) == 7:
                    student = {
                        "name": parts[0],
                        "id": parts[1],
                        "test1": float(parts[2]),
                        "test2": float(parts[3]),
                        "test3": float(parts[4]),
                        "average": float(parts[5]),
                        "grade": parts[6]
                    }

                    students.append(student)

    except IOError:
        print("Error: Could not load student records.")
    except ValueError:
        print("Error: Some saved student data was not valid.")

    return students

def save_students_to_file(students):
    try:
        with open(DATA_FILE, "w") as file:
            for student in students:
                line = (
                    student["name"] + "|" +
                    student["id"] + "|" +
                    format(student["test1"], ".2f") + "|" +
                    format(student["test2"], ".2f") + "|" +
                    format(student["test3"], ".2f") + "|" +
                    format(student["average"], ".2f") + "|" +
                    student["grade"]
                )

                file.write(line + "\n")

        print("Student records have been saved to", DATA_FILE)

    except IOError:
        print("Error: Could not save student records.")

def add_student(students):
    print("\nAdd New Student")

    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")

    try:
        test1 = float(input("Enter Test 1 score: "))
        test2 = float(input("Enter Test 2 score: "))
        test3 = float(input("Enter Test 3 score: "))

        average = calculate_average(test1, test2, test3)
        grade = determine_letter_grade(average)

        student = {
            "name": name,
            "id": student_id,
            "test1": test1,
            "test2": test2,
            "test3": test3,
            "average": average,
            "grade": grade
        }

        students.append(student)

        print("\nStudent added successfully.")

    except ValueError:
        print("\nInvalid score. Please enter numbers only.")

def display_all_students(students):
    if len(students) == 0:
        print("\nNo student records to display.")
        return

    print("\nAll Students")
    print("-" * 80)
    print(f"{'Name':20} {'ID':10} {'Test1':>8} {'Test2':>8} {'Test3':>8} {'Average':>8} {'Grade':>6}")
    print("-" * 80)

    for student in students:
        print(f"{student['name']:20} {student['id']:10} {student['test1']:8.2f} {student['test2']:8.2f} {student['test3']:8.2f} {student['average']:8.2f} {student['grade']:>6}")

    print("-" * 80)

def search_student_by_name(students):
    if len(students) == 0:
        print("\nNo student records to search.")
        return

    name_to_search = input("\nEnter student name to search: ").lower()

    found = False

    for student in students:
        if student["name"].lower() == name_to_search:
            print("\nStudent Found")
            print("Name:", student["name"])
            print("ID:", student["id"])
            print("Test 1:", format(student["test1"], ".2f"))
            print("Test 2:", format(student["test2"], ".2f"))
            print("Test 3:", format(student["test3"], ".2f"))
            print("Average:", format(student["average"], ".2f"))
            print("Grade:", student["grade"])
            found = True

    if found == False:
        print("\nNo student found with that name.")

def display_class_statistics(students):
    if len(students) == 0:
        print("\nNo student records. Cannot calculate statistics.")
        return

    highest = students[0]
    lowest = students[0]
    total = 0

    for student in students:
        total = total + student["average"]

        if student["average"] > highest["average"]:
            highest = student

        if student["average"] < lowest["average"]:
            lowest = student

    class_average = total / len(students)

    print("\nClass Statistics")
    print("-" * 40)
    print("Highest Average:", format(highest["average"], ".2f"), "-", highest["name"])
    print("Lowest Average :", format(lowest["average"], ".2f"), "-", lowest["name"])
    print("Class Average  :", format(class_average, ".2f"))
    print("-" * 40)

def print_menu():
    print("\nStudent Grade Calculator")
    print("-" * 30)
    print("1. Add New Student")
    print("2. Display All Students")
    print("3. Search Student by Name")
    print("4. View Class Statistics")
    print("5. Save and Exit")
    print("Type ESC to save and exit.")

def main():
    students = load_students_from_file()

    while True:
        print_menu()

        choice = input("\nEnter your choice (1-5 or ESC): ")

        if choice.upper() == "ESC":
            save_students_to_file(students)
            print("Exiting program.")
            break
        elif choice == "1":
            add_student(students)
        elif choice == "2":
            display_all_students(students)
        elif choice == "3":
            search_student_by_name(students)
        elif choice == "4":
            display_class_statistics(students)
        elif choice == "5":
            save_students_to_file(students)
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please choose 1-5 or ESC.")

if __name__ == "__main__":
    main()
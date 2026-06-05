# TASK 2 - STUDENT GRADE TRACKER

# Dictionary to store student data
students = {}

while True:

    print("\n===== STUDENT GRADE TRACKER =====")
    print("1. Add Student")
    print("2. View Student Record")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # ADD STUDENT
    if choice == "1":

        name = input("Enter Student Name: ")

        subjects = int(input("Enter Number of Subjects: "))

        marks_list = []

        # Input grades for subjects
        for i in range(subjects):

            marks = float(input(f"Enter marks for Subject {i + 1}: "))
            marks_list.append(marks)

        # Calculate average
        average = sum(marks_list) / len(marks_list)

        # Store data
        students[name] = {
            "Marks": marks_list,
            "Average": average
        }

        print("Student record added successfully!")

    # VIEW RECORD
    elif choice == "2":

        name = input("Enter Student Name: ")

        if name in students:

            print("\n===== STUDENT REPORT =====")

            print("Name:", name)
            print("Marks:", students[name]["Marks"])

            print("Average:", round(students[name]["Average"], 2))

        else:
            print("Student record not found!")

    # EXIT
    elif choice == "3":

        print("Program Closed.")
        break

    else:
        print("Invalid Choice! Try Again.")
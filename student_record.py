def show_menu():
    print("\n==== Student Record Manager ====")
    print("1. View Student")
    print("2. Update Score")
    print("3. Add New Field")
    print("4. Remove Field")
    print("5. Show Keys")
    print("6. Show Values")
    print("7. Exit")


def view_student(student):
    print("\nStudent Information")
    for key, value in student.items():
        print(f"{key.title()}: {value}")


def update_score(student, score):
    student["score"] = score
    print("Score updated successfully.")


def add_new_field(student, key, value):
    student[key] = value
    print(f"{key} added successfully.")


def remove_field(student, key):
    if key in student:
        student.pop(key)
        print(f"{key} removed successfully.")
    else:
        print(f"{key} does not exist.")


def show_keys(student):
    print("\nKeys:")
    for key in student.keys():
        print(key)


def show_values(student):
    print("\nValues:")
    for value in student.values():
        print(value)


student = {
    "name": "Michael",
    "age": 30,
    "course": "Python",
    "score": 85
}

while True:
    show_menu()

    choice = input("Select an option: ").strip()

    if choice == "1":
        view_student(student)

    elif choice == "2":
        score = int(input("Enter new score: ").strip())
        update_score(student, score)

    elif choice == "3":
        key = input("Enter field name: ").strip()
        value = input("Enter value: ").strip()
        add_new_field(student, key, value)

    elif choice == "4":
        key = input("Enter field to remove: ").strip()
        remove_field(student, key)

    elif choice == "5":
        show_keys(student)

    elif choice == "6":
        show_values(student)

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Please select a valid option.")

# Personal Utility Library/
# │
# ├── main.py
# ├── math_utils.py
# └── string_utils.py
# ├── menu.py(Refactor) refactor into this (menu.py) later

import math_utils
import string_utils


def show_menu():
    print("\n==== Personal Utility Library ====")
    print("1. Math Operations")
    print("2. String Operations")
    print("3. Exit")


def math_operations():

    while True:
        math_utils.math_menu()

        operation = input("Select an operation: ").strip()

        if operation == "5":
            return

        if operation == "6":
            return "exit"

        if operation not in ("1", "2", "3", "4"):
            print("Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))

        except ValueError:
            print("Please enter numbers only.")
            continue

        if operation == "1":
            result = math_utils.add(num1, num2)

        elif operation == "2":
            result = math_utils.subtract(num1, num2)

        elif operation == "3":
            result = math_utils.multiply(num1, num2)

        elif operation == "4":
            result = math_utils.divide(num1, num2)

        print(f"Result: {result}")


def string_operations():

    while True:
        string_utils.string_menu()

        operation = input("Select an operation: ").strip()

        if operation == "5":
            return

        if operation == "6":
            return "exit"

        if operation not in ("1", "2", "3", "4"):
            print("Please select a valid option.")
            continue

        text = input("Enter text: ").strip()

        if operation == "1":
            result = string_utils.uppercase(text)

        elif operation == "2":
            result = string_utils.lowercase(text)

        elif operation == "3":
            result = string_utils.count_characters(text)

        elif operation == "4":
            result = string_utils.reverse_text(text)

        print(f"Result: {result}")


def main():

    while True:

        show_menu()

        choice = input("Select an option: ").strip()

        if choice == "1":

            result = math_operations()

            if result == "exit":
                break

        elif choice == "2":

            result = string_operations()

            if result == "exit":
                break

        elif choice == "3":

            print("Goodbye!")
            break

        else:
            print("Please select a valid option.")


if __name__ == "__main__":
    main()
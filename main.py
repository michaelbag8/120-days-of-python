# Personal Utility Library

import math_utils
import string_utils


MATH_OPERATIONS = {
    "1": math_utils.add,
    "2": math_utils.subtract,
    "3": math_utils.multiply,
    "4": math_utils.divide,
}

STRING_OPERATIONS = {
    "1": string_utils.uppercase,
    "2": string_utils.lowercase,
    "3": string_utils.count_characters,
    "4": string_utils.reverse_text,
}


def show_menu():
    print("\n==== Personal Utility Library ====")
    print("1. Math Operations")
    print("2. String Operations")
    print("3. Exit")


def handle_back_or_exit(operation):
    if operation == "5":
        return False
    if operation == "6":
        return "exit"
    return None


def math_operations():
    while True:
        math_utils.math_menu()

        operation = input("Select an operation: ").strip()
        action = handle_back_or_exit(operation)

        if action is not None:
            return action

        if operation not in MATH_OPERATIONS:
            print("Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        result = MATH_OPERATIONS[operation](num1, num2)
        print(f"Result: {result}")


def string_operations():
    while True:
        string_utils.string_menu()

        operation = input("Select an operation: ").strip()
        action = handle_back_or_exit(operation)

        if action is not None:
            return action

        if operation not in STRING_OPERATIONS:
            print("Please select a valid option.")
            continue

        text = input("Enter text: ").strip()
        result = STRING_OPERATIONS[operation](text)
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
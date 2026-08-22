ho#Challenge (Refactoring)
#Can you rewrite your program so that the two numbers are requested only once?
#Hint:
#if operation in ("1", "2", "3", "4"):
    # Ask for the numbers here
#Then, inside each branch, simply call the correct function.
#This will make your code shorter, cleaner, and easier to maintain.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero."
    return a / b


def show_menu():
    print("\n==== Simple Calculator ====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


while True:
    show_menu()

    operation = input("Select an option: ").strip()

    if operation == "5":
        print("Goodbye!")
        break

    if operation not in ("1", "2", "3", "4"):
        print("Please select a valid option.")
        continue

    number_one = float(input("Enter first number: "))
    number_two = float(input("Enter second number: "))

    if operation == "1":
        result = add(number_one, number_two)

    elif operation == "2":
        result = subtract(number_one, number_two)

    elif operation == "3":
        result = multiply(number_one, number_two)

    elif operation == "4":
        result = divide(number_one, number_two)

    print(f"Result: {result}")

#mini calculator using class
# Define and initialize the Calculator class
class Calculator:
  def __init__(self, num_one, num_two):
    self.num_one = num_one
    self.num_two = num_two
  
  # Create the addition method
  def addition(self):
    return self.num_one + self.num_two
  
  # Create the subtraction method
  def subtraction(self):
    return self.num_one - self.num_two
  
  # Create the multiplication method
  def multiplication(self):
    return self.num_one * self.num_two   

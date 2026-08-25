print("=====List Analyzer=====")

def numbers_list():
    try:
        numbers = list(map(int, input("Enter Numbers: ").split()))
    except ValueError:
        return None
    return numbers


numbers = numbers_list()
if numbers is None:
    print("Please enter a list of numbers separated by space")
elif not numbers:
    print("No numbers entered.")
else:
    reversed_numbers = list(reversed(numbers))
    sorted_numbers = sorted(numbers)

    print("Numbers: ", numbers)
    print("Count: ", len(numbers))
    print("Maximum: ", max(numbers))
    print("Minimum: ", min(numbers))
    print("Sum: ", sum(numbers))
    print("Sorted: ", sorted_numbers)
    print("Reversed: ", reversed_numbers)

print("=====List Analyzer=====")

def numbers_list():
    numbers = list(map(int, input("Enter Numbers: ").split()))
    return numbers


numbers = numbers_list()

if not numbers:
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

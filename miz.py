def find_missing_number(numbers):
    to_set = set(numbers)

    missing_number = 1
    while missing_number in to_set:
        missing_number += 1
    return missing_number

numbers = [3, 4, -1, 1]
print(find_missing_number(numbers))


def create_list(n):
    return [[n] for _ in range(5)]

print(create_list(3))

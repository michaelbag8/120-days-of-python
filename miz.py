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

def remove_vowels(string):
    vowel = "aeiou"
    new_word = ""
    for letters in string:
        if not letters in vowel:
            new_word += letters
    return new_word

word = "hello"
print(remove_vowels(word))
import math
def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return round(area, 2)

def convert_to_camel_case(s: str) -> str:
    words = s.split()
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])


def repeat_item(item, n):
    return list(item*n)

def calculate_clock_interval(face1, face2):
    difference = abs(face1- face2)
    return min(difference, 12-difference)


def find_square_root(n):
    square_root = math.sqrt(n)
    return round(square_root, 2)

def is_spongecase(s):
    for index, letter in enumerate(s):
        if index % 2 == 0:
            if letter.isupper() != s[0].isupper():
                return False
        else:
            if letter.isupper() == s[0].isupper():
                return False

    return True

def power_of_two(n):
    return 2 ** n

print(power_of_two(3))
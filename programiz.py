import math
def calculate_area(radius):
    area = math.pi * (radius ** 2)
    return round(area, 2)

def convert_to_camel_case(s: str) -> str:
    words = s.split()
    return words[0].lower() + "".join(word.capitalize() for word in words[1:])

print(convert_to_camel_case("hello world"))

def repeat_item(item, n):
    return list(item*n)

def calculate_clock_interval(face1, face2):
    difference = abs(face1- face2)
    return min(difference, 12-difference)


def find_square_root(n):
    square_root = math.sqrt(n)
    return round(square_root, 2)
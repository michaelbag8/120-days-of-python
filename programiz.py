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
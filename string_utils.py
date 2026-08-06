def string_menu():
    
    print("\n==== String Operations ====")
    print("1. Uppercase")
    print("2. Lowercase")
    print("3. Count Characters")
    print("4. Reverse Text")
    print("5. Back")
    print("6. Exit")


def uppercase(text):
    return text.upper()


def lowercase(text):
    return text.lower()


def count_characters(text):
    return len(text)


def reverse_text(text):
    return text[::-1]

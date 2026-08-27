#mini count down
number = int(input("Enter starting number: "))

while number >= 1:
    print(number)
    number -= 1

def count_down(number):
    if number < 0:
        return
    print(number)
    count_down(number - 1)


def main():
    try:
        number = int(input("Enter a starting number: "))
    except ValueError:
        print("That's not an integer.")
        return
    count_down(number)


main()
print("Blast Off!")

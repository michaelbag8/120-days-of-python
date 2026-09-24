import time


def count_down(start):
    if start < 0:
        print("Please enter a non-negative number.")
        return

    for number in range(start, -1, -1):
        print(f"\r{number:02d}", end="", flush=True)
        time.sleep(0.5)

    print("\rBlast Off!")


def main():
    try:
        number = int(input("Enter a starting number: "))
    except ValueError:
        print("That's not an integer.")
        return

    count_down(number)


if __name__ == "__main__":
    main()

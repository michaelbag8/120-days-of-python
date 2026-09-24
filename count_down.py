import time


def format_time(total_seconds):
    minutes, seconds = divmod(total_seconds, 60)
    return f"{minutes:02d}:{seconds:02d}"


def count_down(start):
    if start < 0:
        print("Please enter a non-negative number.")
        return

    for remaining in range(start, -1, -1):
        print(f"\r{format_time(remaining)}", end="", flush=True)
        time.sleep(0.5)

    print("\r00:00")
    print("Blast Off!")


def main():
    try:
        seconds = int(input("Enter a starting number in seconds: "))
    except ValueError:
        print("That's not an integer.")
        return

    count_down(seconds)


if __name__ == "__main__":
    main()

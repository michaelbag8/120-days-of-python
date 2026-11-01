numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

expected = sum(
    range(1, len(numbers) + 2)
)

actual = sum(numbers)

missing = expected - actual

print("Numbers:", numbers)
print("Missing Number:", missing)

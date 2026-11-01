numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

expected = sum(
    range(1, len(numbers) + 2)
)

actual = sum(numbers)

missing = expected - actual

print("Numbers:", numbers)
print("Missing Number:", missing)

users = {
    "emma": "Python@123",
    "oliver": "Code#456",
    "sophia": "Dev$789"
}

username = "emma"
password = "Python@123"

attempts = 3
logged_in = False

while attempts > 0:

    if username not in users:
        print("User not found")
        break

    if users[username] == password:
        logged_in = True
        print("Login successful!")
        break

    attempts -= 1
    print(
        f"Incorrect password. "
        f"{attempts} attempt(s) left."
    )

if not logged_in and attempts == 0:
    print("Account temporarily locked.")

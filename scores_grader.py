#mini grader, will be refactor later
score = int(input("Enter a score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")


# learning match case statement 
day = 2

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case _:
        print("Unknown")

point = (3, 4)

match point:
    case (0, 0):
        print("Origin")
    case (x, y):
        print(f"{x}, {y}")

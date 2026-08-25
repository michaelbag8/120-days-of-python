print("=====List Analyzer=====")

def numbers_list():
    num = list(map(int, input("Enter Numbers: ").split()))
    return num


result =  numbers_list()
rev = list(reversed(result))
sor = sorted(result)

print("Numbers: ", result)
print("Count: ", len(result))
print("Maximum: ", max(result))
print("Minimum: ", min(result))
print("Sum: ", sum(result))
print("Sorted: ",sor)
print("Reversed: ", rev)
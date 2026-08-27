#mini count down
number = int(input("Enter starting number: "))

while number >= 1:
    print(number)
    number -= 1

def count_down():
    number= int(input("Enter a starting number: ")           
    if not isintance(number, int):
                return f"{number} is not an integer"          
    if number == 0:
        return 
        print(number)
        count_down(number-1)

                
print(count_down(5))
print("Blast Off!")

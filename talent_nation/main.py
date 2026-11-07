
#Expected totals: Ada 5; John 6; Grace 1.
# Write a function that returns a 
# dictionary of the total quantity per fellow, without hardcoding results.

transactions = [
    {"fellow": "Ada", "quantity": 2},
    {"fellow": "John", "quantity": 4},
    {"fellow": "Ada", "quantity": 3},
    {"fellow": "Grace", "quantity": 1},
    {"fellow": "John", "quantity": 2}
]

def frequency_table(transactions):
    total = {}
    for items in transactions: 
        name = items["fellow"]
        quantity = items["quantity"]
        if name in total:
            total[name] += quantity
        else:
            total[name] = quantity
    return total

print(frequency_table(transactions))


# B1. Trace the code and explain the output
# *
# What exactly is printed, and why?

items = [2, 4, 6]
result = []
for item in items:
    if item % 4 == 0:
        continue
    result.append(item * 2)
print(result)

# Answer:
# What is printed is [4, 12], because for every number in the list that is divisible by 4 is skipped and the rest are multiplied by 2 and are appended to a new list.
# In the list [2,4,6], 2 % 4 and 6 % 4 both leaves a remainder of 2, not 0, therefore they are multiplied by 2 and appended.


# B2. Diagnose and repair a borrowing bug
# *
# Identify the problem, explain its consequences and rewrite the function correctly.

def borrow(resource, quantity):
    resource["available"] -= quantity
    if resource["available"] < 0:
        return "Not enough stock"
    return "Success"

print(borrow(["yam"], 20))


def borrow(resource, quantity):
    if quantity <= 0:
        return "Invalid quantity"
    if quantity > resource["available"]:
        return "Not enough stock"
    resource["available"] -= quantity
    return "Success"

# The function does not check whether there is enough stock, before subtracting the quantity, 
# it does not validates first before changing the data and the consequences of the problems discovered 
# with the function is that stock will be negative , which is not supposed to be so, from the first line 
# resource["available"] -= quantity even if it fails it will state change the data.


# It is unsafe because check and update are not the same step. 
# If Fellow A checks and requests 4 laptops and 5 are available, 
# so it is allowed, then Fellow B checks and also requests 4 laptops, 
# and still 5 are available because Fellow A has not updated yet, 
# so he is allowed too, so by the time Fellow B acts and there is nothing to re-verify, 
# Fellow A will not get his request, although it initially showed him available.
# To ensure no more laptops are issued than available, 
# then check and update should be one step by making sure only 
# one request can enter the check and update section while the second one waits
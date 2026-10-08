
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
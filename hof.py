
# map(function, iterable) — applies function to every item, lazy
nums = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, nums)
print(list(squared))    # [1, 4, 9, 16]

# filter(function, iterable) — keeps items where function(item) is True
evens = filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6])
print(list(evens))      # [2, 4, 6]

# functools.reduce(function, iterable, initializer=None) — collapses to one value
from functools import reduce
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(total)             # 10

#
def make_adder(n):
    return lambda x: x + n
add5 = make_adder(5)
add10 = make_adder(10)
print(add5(1), add10(1))


def outer():
    x = 10
    def inner():
        return x
    x = 20
    return inner
f = outer()
print(f())

#Mini Project
#Build a pipeline tool: pipeline(data, *functions) runs data through a chain of functions, each output feeding the next. Use it to process raw scores:
raw_scores = ["  85", "92 ", " 78", "100", " 65 "]
# Steps: strip whitespace → convert to int → filter out below 70 → average what remains

def counter():
    count = 0
    def increment():
        count += 1
        return count
    return increment
c = counter()
print(c())

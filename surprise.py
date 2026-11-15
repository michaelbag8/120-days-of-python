from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
print(fibonacci(50))
print(fibonacci(100))

class User:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("Name must be a string")

        if not new_name.strip():
            raise ValueError("Name cannot be empty")

        self._name = new_name
class Age:
    def __get__(self, instance, owner):
        return 25

    def __set__(self, instance, value):
        print(f"Age assigned: {value}")


class Person:
    age = Age()


person = Person()

person.age = 30

print(person.age)


@lru_cache(maxsize=None)
def square(n):
    print("Calculating...")
    return n * n


print(square(5))
print(square(5))
print(square(5))

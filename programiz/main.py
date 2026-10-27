import statistics

def find_smallest(lists):
    return [min(outer_list) for outer_list in lists]
    

def find_standard_deviation(numbers):
    return round(statistics.stdev(numbers), 2)


def count_parameters(*args):
    return len(args)


def find_vowel_words(sentence):
    vowel = []
    vowels = "aeiouAEIOU"
    words = sentence.split(" ")
    for letters in words:
        for l in vowels:
            if letters.startswith(l):
                vowel.append(letters)
    return vowel


def match_last_item(lst):
    if "".join(lst[:-1]) == lst[-1]:
        return True
    return False
   

def memorial_cost(prices):
    split_ = prices.split(" ")
    total = 0
    for n in split_:
        total += int(n)
    return total

def sum_of_squares(numbers):
    return sum([n**2 for n in numbers])

def number_to_dashes(n):
    return "-" * n
    
def repeat_last_char(string, n):
    return string[:-1] + string[-1]*n

def factorial(n):
    if n ==0:
        return 1
    return factorial(n-1) * n



inputs = ['a', 'b', 'c', 'd','abcd']

out = ["abc", "def", "ghi", "abcdefghis"]

sentence = "I How AM my Emmannuel friend Enyung"
std = [1,2,3,4,5]
lst = [[1,2,3], [4,5,6], [7,8,9]]
ls = [[10, 20], [30, 40], [50, 60]]


print(find_smallest(lst))
print(find_smallest(ls))
print(find_standard_deviation(std))
print(count_parameters(1,2,3,4,5,6))
print(find_vowel_words(sentence))
print(match_last_item(out))
print(memorial_cost('10 20 30 40'))
print(sum_of_squares([2,3,4]))
print(number_to_dashes(5))
print(repeat_last_char("hello", 3))
print(factorial(5))

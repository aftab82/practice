"""
Problem:
Write a program which will find all the numbers between 1000 and 5000 (both included)
Such that each digit of a number is an even number.
The numbers obtained should be printed in a comma separated sequence on a single line.
"""


def find_nums(a, b):
    res = []
    for num in range(a, b + 1):
        is_even = True
        for digit in str(num):
            if int(digit) % 2 != 0:
                is_even = False
        if is_even:
            res.append(num)
    return res


print(*find_nums(1000, 5000), sep=', ')

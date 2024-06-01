


import math

def fac(k):
    factorial = 1
    for i in range(1, k):
        factorial *= i
    return factorial

for i in range(27):
    factorial = fac(i)

    print(f"{i}! is {factorial}")
    G={
        1:[12,2,34],
        2:[1],

    }
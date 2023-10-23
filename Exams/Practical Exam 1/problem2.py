"""
problem2
Author: Quang Huynh
"""

import turtle as t

def squares_iter(side, num):
    total = 0
    while num > 0:
        t.fd(side)
        t.left(90)
        t.fd(side)
        t.left(90)
        t.fd(side)
        t.left(90)
        t.fd(side)
        t.left(90)
        num -= 1
        total += side * 4
        side -= 10
    return total



side = int(input("Size of square?: "))
num = int(input("Depth?: "))
total1 = 0
total1 += squares_iter(side, num)
print("Total length: " + str(total1))
t.done()

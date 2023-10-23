"""
problem1
Author: Quang Huynh
"""

import turtle as t


def init(size):
    t.reset()
    t.setup(600,600)
    t.setworldcoordinates(-2*size, -2*size, 2*size, 2*size)
    t.speed(0)
    t.pensize(2)

def problem1(levels, size):
    if levels == 0:
        return
    else:
        t.left(45)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.left(90)
        t.fd(size)
        t.left(90)
        t.right(90)
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.right(90)
        t.fd(size)
        t.right(45)
        problem1(levels - 1, size / 2)



def main():
    levels = int(input("How many levels?: "))
    size = int(input("Size of square?: "))
    init(size)
    problem1(levels, size)
    t.done()


if __name__ == "__main__":
    main()

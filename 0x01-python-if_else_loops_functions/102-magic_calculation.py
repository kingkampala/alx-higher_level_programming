#!/usr/bin/python
def magic_calculation(a, b, c):
    if a < b:
        return c
    if b < c:
        return a + b
    return a * b - c

#!/usr/bin/python3
def no_c(my_string):
    table = my_string.translate({ord('c'): '', ord('C'): ''})
    return (table)

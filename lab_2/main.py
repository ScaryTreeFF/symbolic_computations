from fractions import Fraction
import re

"""
Representation:
−E, E − F, E/F as, respectively, (−1)⋅E, E + (−1)⋅F, E⋅F−1
a + b + c as "+"(a, b, c)
"""

def Symbol(symbol):
    return symbol

def parseTex(input_data):
    # setup
    funcs_with_args = ('frac', 'sqrt')
    simple_funcs = ('+', '-', '*', '/', '^')
    func_escape = '\\'
    input_data = input_data.strip('$')

    for idx, current_symbol in enumerate(input_data):
        if current_symbol == func_escape:
            # find function with args and run recursion
            pass
        elif current_symbol in simple_funcs:
            # get function and its arguments
            func = current_symbol
            first_arg  = input_data[:idx]
            second_arg = input_data[idx+1:]
            # we need to recursively call our parse func
            pass
    r"^\$\$$"
    pass

def simplify(input_data):
    pass
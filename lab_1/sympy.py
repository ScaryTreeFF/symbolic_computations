from sympy import *

init_printing(use_unicode=False, wrap_line=False)
x = Symbol('x')
integrate(x**2 + x + 1, x)

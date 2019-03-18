from expression import Expression, Context

ctx = Context()
expr_in = 0
while expr_in != 'exit':
    expr_in = input()
    if expr_in == 'exit':
        break
    eq_pos = expr_in.find('=')
    if eq_pos == -1:
        expr = Expression(expr_in, ctx)
        if str(expr) != 'error':
            print(expr)
    else:
        func = expr_in[0:eq_pos - 1]
        name = func[:-3]
        symbol = func[-2]
        ctx.add_func(name, expr_in[eq_pos + 2:], symbol)

# remember our new symbol 
# then try to plot it:
#   Expression: 
#       try to parse it in f_parser
#       create new Expression
#       simplify
#       plot
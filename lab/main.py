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
        ctx.add_func(expr_in[0:eq_pos - 1], expr_in[eq_pos + 2:])

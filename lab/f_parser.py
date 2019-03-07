def parse(input_expr: str):

    __viable_functions = [
        'add',
        'mul',
        'pow',
        'div',
        'simplify',
        'plot'
    ]

    __func_dict = {
        'add': '+',
        'mul': '*',
        'pow': '^',
        'div': '/'
    }

    def is_func(text: str):
        pos = text.find('(')
        if pos == -1 or text[0:pos] not in __viable_functions or text[-1] != ')':
            return False
        else:
            return True

    def find_comma(text: str):
        pos_par = text.find('(')
        pos = text.find(',')
        if pos_par != -1 and pos_par < pos:
            par_open = 1
            i = pos_par
            while par_open != 0:
                i += 1
                if text[i] == '(':
                    par_open += 1
                if text[i] == ')':
                    par_open -= 1
            pos = i + 1
        else:
            pos = text.find(',')
        if pos != -1:
            return pos
        else:
            return -1


    if is_func(input_expr):
        pos_par = input_expr.find('(')
        args = input_expr[pos_par + 1:-1]
        if input_expr[0:pos_par] == 'simplify':
            return 'symp', args, None, None
        comma_pos = find_comma(args)
        if comma_pos != -1:
            if input_expr[0:pos_par] == 'plot':
                pos_comma1 = comma_pos
                pos_comma2 = args.find(',', pos_comma1 + 1)
                pos_comma3 = args.find(',', pos_comma2 + 1)
                pos_comma4 = args.find(',', pos_comma3 + 1)
                expr_str = args[:pos_comma1]
                x = args[pos_comma1 + 2:pos_comma2]
                y = args[pos_comma2 + 2:pos_comma3]
                var1 = args[pos_comma3 + 2:pos_comma4]
                var2 = args[pos_comma4 + 2:]
                return 'plot' + var1 + var2, expr_str, x, y
            else:
                arg1 = args[0:comma_pos]
                arg2 = args[comma_pos + 2:]
                return 'func', __func_dict[input_expr[0:pos_par]], arg1, arg2
        else:
            return -1
    elif input_expr.isnumeric() or (input_expr[1:].isnumeric() and input_expr[0] == '-'):
        return 'value', int(input_expr), None, None
    elif input_expr.isalnum():
        return 'symbol', input_expr, None, None

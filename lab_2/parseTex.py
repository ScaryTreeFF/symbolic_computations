from fractions import Fraction
import re

"""
Representation:
−E, E − F, E/F as, respectively, (−1)⋅E, E + (−1)⋅F, E⋅F−1
a + b + c as "+"(a, b, c)

['function', arg1, arg2, arg3, ...]
"""

def Symbol(symbol):
    return symbol

def deleteOuterBrackets(data):
    return data[2:-2]

def findLeftArg(data):
    pass

def findRightArg(data):
    pass

def findTwoArgs(data):
    print(f'Data inside findTwoArgs: {data}')
    count_brackets = 0
    flag_found_bracket = False

    for idx, symbol in enumerate(data):
        if count_brackets == 0 and flag_found_bracket:
            div_idx = idx
            break
        if symbol == '{':
            count_brackets += 1
            flag_found_bracket = True
            continue
        elif symbol == '}':
            count_brackets -= 1
            flag_found_bracket = True
            continue
    first_arg = deleteOuterBrackets(data[:div_idx])
    second_arg = deleteOuterBrackets(data[div_idx:])
    print(f'Returning arguments: {first_arg} -- {second_arg}')
    return first_arg, second_arg
            

def parseTex(input_data):
    # setup
    funcs_with_args = ('frac', 'sqrt', 'sin', 'cos', 'tan', 'ln', 'log')
    simple_funcs = { "+": 0, "-": 0, "*": 1, "/": 1, "^": 1}
    func_escape = '\\'
    input_data = input_data.strip('$')
    inner_view = []

    def parseInner(data):
        print(f'Parsing: {data}')
        symbol = re.match(r'^({.})+$', data)
        if symbol is not None:
            symbol = re.sub(r'{|}', '', symbol.group(0))
            if len(symbol) == 1:
                return int(symbol)
            ret_val = []
            for x in symbol:
                try:
                    int(x)
                    ret_val.append(int(x))
                except:
                    ret_val.append(['symbol', x])
            ret_val.insert(0, '*')
            return(ret_val)
            
        arg = None
        for idx, current_symbol in enumerate(data):
            # print(f'{idx}: {current_symbol}')
            if current_symbol == func_escape:
                # find function 
                func = re.match(r"[a-zA-z]+", data[idx+1:])
                if func is None:
                    print ('Not functions found!')
                    raise Exception
                else:
                    func = func.group(0)
                    rest = data[idx+1+len(func):]

                # find arg in rest
                if func == 'frac':
                    first_arg, second_arg = findTwoArgs(rest)
                elif func == 'log':
                    arg = ''
                    for symbol in rest:
                        if symbol == ' ':
                            break
                        if symbol == '_':
                            continue
                        arg += symbol
                    arg = int(arg)
                else:
                    # find one arg (just delete '{}')
                    arg = deleteOuterBrackets(rest)
                    print(f'Found that arg: {arg}')

                
            elif current_symbol in simple_funcs:
                # TODO make priorities of operands
                # get function and its arguments
                func = current_symbol
                first_arg  = data[:idx]
                second_arg = data[idx+1:]
            else:
                continue

            # run recursion
            print(f'CURRENT INNER VIEW: {inner_view}')
            if arg is not None:
                inner_view.append([func, parseInner(arg)])
            else:
                inner_view.append([func, parseInner(first_arg), parseInner(second_arg)])

    parseInner(input_data)
            
    return inner_view
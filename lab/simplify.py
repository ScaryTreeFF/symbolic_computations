from copy import deepcopy


def simplify_add(expr):
    temp_list = []
    for i in range(len(expr.args)):
        if expr.args[i] != -1:
            temp_list.append(expr.args[i])
            if expr.args[i].is_monomial:
                for j in range(i + 1, len(expr.args)):
                    if expr.args[j] != -1 and (expr.args[j].variables == temp_list[-1].variables) \
                            and expr.args[j].is_monomial:
                        temp_list[-1].value += expr.args[j].value
                        expr.args[j] = -1
    expr.args = temp_list
    reduce(expr)


def simplify_mul(expr):
    var_exists = False
    expr.value = 1
    for arg in expr.args:
        if arg.is_monomial:
            expr.value *= arg.value
            if len(arg.variables) != 0:
                for var_out in arg.variables:
                    for var_in in expr.variables:
                        if len(var_in) != 0 and var_out[0] == var_in[0]:
                            var_in[1] += var_out[1]
                            var_exists = True
                            break
                    if not var_exists:
                        expr.variables.append(var_out)
    add_func_ind = -1
    for i in range(len(expr.args)):
        if expr.args[i].value == '+':
            add_func_ind = i
            break
    if add_func_ind != -1:
        for i in range(add_func_ind + 1, len(expr.args)):
            if expr.args[i].value == '+':
                merge_add(expr.args[add_func_ind], expr.args[i])
        for i in range(len(expr.args[add_func_ind].args)):
            expr.args[add_func_ind].args[i] *= expr
        temp = expr.args[add_func_ind]
        expr.args = [temp]
        reduce(expr)
        simplify_add(expr)
    else:
        expr.is_monomial = True
        expr.args = []
        if len(expr.variables) > 0:
            expr.type = 'symbol'
        else:
            expr.type = 'value'


def merge_add(expr1, expr2):
    temp_list = []
    for arg1 in expr1.args:
        for arg2 in expr2.args:
            temp_list.append(arg1 * arg2)
    expr1.args = temp_list


def simplify_pow(expr):
    if expr.args[0].type == 'value':
        expr.value = expr.args[0].value ** expr.args[1].value
        expr.type = 'value'
        expr.args = []
        expr.is_monomial = True
    elif expr.args[0].type == 'symbol':
        for var in expr.args[0].variables:
            var[1] *= expr.args[1].value
        expr.value = expr.args[0].value ** expr.args[1].value
        expr.variables = expr.args[0].variables
        expr.type = 'symbol'
        expr.is_monomial = True
        expr.args = []


def simplify_div(expr):
    if expr.args[0].type == 'value':
        expr.value = expr.args[0].value / expr.args[1].value
        expr.type = 'value'
        expr.args = []
        expr.is_monomial = True
    elif expr.args[0].type == 'symbol':
        # for var in expr.args[0].variables:
        #     print(var)
        #     var[1] *= expr.args[1].value
        expr.value = expr.args[0].value / expr.args[1].value
        expr.variables = expr.args[0].variables
        expr.type = 'symbol'
        expr.is_monomial = True
        expr.args = []
        
def extract_args(expr):
    if expr.type != 'func':
        return
    func_exists = False
    for i in range(len(expr.args)):
        if expr.args[i].value == expr.value:
            func_exists = True
            break
    if not func_exists:
        return
    temp_list = []
    for i in range(len(expr.args)):
        if expr.args[i].value == expr.value:
            for j in range(len(expr.args[i].args)):
                temp_list.append(expr.args[i].args[j])
        else:
            temp_list.append(expr.args[i])
    expr.args = deepcopy(temp_list)


def reduce(expr):
    if len(expr.args) == 1:
        expr.value = expr.args[0].value
        expr.type = expr.args[0].type
        expr.variables = expr.args[0].variables
        expr.is_monomial = expr.args[0].is_monomial
        expr.args = expr.args[0].args
        return 0
    else:
        return -1


def simplify(expr):
    for arg in expr.args:
        if arg.type == 'func':
            simplify(arg)
    extract_args(expr)
    if expr.value == '+':
        simplify_add(expr)
    elif expr.value == '*':
        simplify_mul(expr)
    elif expr.value == '^':
        simplify_pow(expr)
    elif expr.value == '/':
        simplify_div(expr)

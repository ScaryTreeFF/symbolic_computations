from f_parser import parse
from context import Context
from simplify import simplify
from copy import deepcopy
from error_out import input_error_message
from my_plot import plot


class Expression:
    def __init__(self, data: str, ctx: Context):
        self.args = []
        self.is_monomial = False
        self.variables = []
        try:
            self.type, self.value, arg1, arg2 = parse(data)
        except(TypeError):
            input_error_message(data)
            self.type = 'error'
            return
        if self.type == 'symp':
            expr = Expression(self.value, ctx)
            simplify(expr)
            self.__clone(expr)
        elif self.type[0:4] == 'plot':
            expr = Expression(self.value, ctx)
            simplify(expr)
            plot(expr, arg1, arg2, self.type[4], self.type[5])
        elif self.type == 'func':
            for arg in (arg1, arg2):
                self.__get_args(arg, self.value, ctx)
        elif self.type == 'symbol':
            expr = ctx.get_func_from_list(self.value)
            if expr != -1:
                expr = Expression(expr, ctx)
                self.__clone(expr)
            else:
                self.variables.append([self.value, 1])
                self.value = 1
                self.is_monomial = True
        else:
            self.is_monomial = True

    def __get_args(self, data, op, ctx):
        _, arg_value, arg1, arg2 = parse(data)
        func = ctx.get_func_from_list(arg_value)
        if func != -1:
            _, arg_value, arg1, arg2 = parse(func)
        if arg_value == op:
            for arg in (arg1, arg2):
                self.__get_args(arg, arg_value, ctx)
        else:
            self.args.append(Expression(data, ctx))

    def substitute(self, arg1, arg2, var1, var2):
        if self.value == '+':
            result = 0
            for arg in self.args:
                result += arg.substitute(arg1, arg2, var1, var2)
            return result
        else:
            result = self.value
            for var in self.variables:
                if var[0] == var1:
                    result *= (arg1 ** var[1])
                if var[0] == var2:
                    result *= (arg2 ** var[1])
            return result

    def __clone(self, expr):
        self.args = deepcopy(expr.args)
        self.value = expr.value
        self.type = expr.type
        self.is_monomial = expr.is_monomial
        self.variables = deepcopy(expr.variables)

    def __mul__(self, other):
        var_exists = False
        result = Expression('1', Context())
        result.value = self.value * other.value
        result.variables = deepcopy(self.variables)
        if len(other.variables) != 0:
            for var_out in other.variables:
                for var_in in result.variables:
                    if len(var_in) != 0 and var_out[0] == var_in[0]:
                        var_in[1] += var_out[1]
                        var_exists = True
                        break
                if not var_exists:
                    result.variables.append(var_out)
        return result

    def __str__(self):
        if self.type == 'error':
            return 'error'
        math_str = ''
        if self.is_monomial:
            if not (self.value == 1 and len(self.variables) != 0):
                math_str += str(self.value)
            for var in self.variables:
                math_str += var[0]
                if var[1] != 1:
                    math_str += ('^' + str(var[1]))
        elif self.type == "func":
            for expr in self.args:
                if len(math_str) != 0:
                    if self.value == '+' and isinstance(expr.value, int) and expr.value < 0:
                        pass
                    else:
                        math_str += (str(self.value))
                math_str += expr.__str__()
        else:
            math_str += str(self.value)
        return math_str

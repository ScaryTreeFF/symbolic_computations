class Context:
    def __init__(self):
        self.__user_functions = []

    def add_func(self, symb, expr, var):
        self.__user_functions.append((symb, expr, var))

    def get_func_from_list(self, key):
        try:
            key, new_var = key.split('[')
            new_var = new_var[-2]
            for symb, expr, var in self.__user_functions:
                if symb == key:
                    expr = expr.replace(var, new_var)
                    var = new_var
                    return expr
        except: 
            pass
        return -1

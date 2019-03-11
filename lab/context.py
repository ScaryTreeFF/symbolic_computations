class Context:
    def __init__(self):
        self.__user_functions = []

    def add_func(self, symb, expr):
        self.__user_functions.append((symb, expr))

    def get_func_from_list(self, key):
        for symb, expr in self.__user_functions:
            if symb == key:
                return expr
        return -1

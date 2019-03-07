class Context:
    def __init__(self):
        self.__user_functions = []
        self.func_list = []

    def add_func(self, symb, expr):
        self.__user_functions.append((symb, expr))

    def get_func_from_list(self, symb):
        for var in self.__user_functions:
            if symb == var[0]:
                return var[1]
        return -1

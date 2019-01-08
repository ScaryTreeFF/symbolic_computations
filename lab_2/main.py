from parseTex import parseTex
from symbol import Symbol

def simplify(input_data):
    pass

def diffAlgo(data):
    diff_table = {
        '^':    powDiff,
        'log':  logDiff,
        'ln':   lnDiff,
        'sin':  sinDiff,
        'cos':  cosDiff,
        'sqrt': sqrtDiff,
        'tan':  tanDiff
    }

    def constDiff(data):
        # 1
        assert int(data) == data
        data = 0
        return data

    def symbolDiff(data):
        assert isinstance(data, Symbol)
        data = 1
        return data

    def powDiff(data):
        # 2, 3, 4
        if isinstance(data[1], Symbol):
            # 2
            data[1] = ['*', data[2], data[1]]
            data[2] = ['-', data[2], 1]
        elif isinstance(data[2], Symbol):
            # 3
            data = ['*', data, ['ln', data[1]]]
        return data

    def logDiff(data):
        # 5
        return data

    def lnDiff(data):
        # 6
        data = ['frac', 1, data[1]]
        return data

    def sinDiff(data):
        # 7
        data[0] = 'cos'
        return data

    def cosDiff(data):
        # 8
        return data

    def sqrtDiff(data):
        # 9
        data = ['frac', 1, ['*', 2, ['sqrt', data[1]]]]
        return data

    def tanDiff(data):
        # 10
        data = ['frac', 1, ['^', ['cos', data[1]],2]]
        return data


# diff_table = {
#     '^': '',
#     'ln': ['frac', 1, arg],

# }

f = open('example1.tex', 'r').read()
inner_view = parseTex(f)
print(inner_view)
# x = Symbol('x')
# print(1 if isinstance(x, Symbol) else 0)
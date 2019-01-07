from parseTex import parseTex

def simplify(input_data):
    pass

f = open('example1.tex', 'r').read()
inner_view = parseTex(f)
print(inner_view)
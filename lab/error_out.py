def input_error_message(data):
    with open('decoration.txt', 'r') as file:
        print(file.read())
        print('Incorrect data in:', '|' + data + '|')

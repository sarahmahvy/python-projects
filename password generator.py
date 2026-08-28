import random


def password_generator (code):
    if isinstance(code, int):
        if len(str(code)) != 16:
            return 'The code should be a 16 charachters long.'
        code = str(code)
    if isinstance (code, str):
        if len(code) != 16:
            return 'The code should be a 16-characters long.'
        code_list = list(code)
        random.shuffle(code_list)
        password = ''.join(code_list)
        return 'your password is:' +password


print(password_generator(input(str('Enter your 16 character code: '))))
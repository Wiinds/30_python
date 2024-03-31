import string
import secrets


def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    
    return False


def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    
    return False


def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    if length <= 3 and (symbols and uppercase):
        raise ValueError('Length must be greater than 3 for symbols and uppercase requirements.')
    
    combination: str = string.ascii_lowercase + string.digits
    new_password: str = ''
    
    if symbols:
        combination += string.punctuation
        new_password += secrets.choice(string.punctuation)
        
    if uppercase:
        combination += string.ascii_uppercase
        new_password += secrets.choice(string.punctuation)
    
    #* Calculate remaining length after adding required characters
    remaning_length = length - len(new_password)
    
    for _ in range(remaning_length):
        new_password += secrets.choice(combination)
    
    new_password_list = list(new_password)
    secrets.SystemRandom().shuffle(new_password_list)
    new_password = ''.join(new_password_list)
    
    return new_password

if __name__ == '__main__':
    for i in range(1, 7):
        new_pass: str = generate_password(length=4, symbols=True, uppercase=True)
        specs: str = f'U: {contains_upper(new_pass)}, S:{contains_symbols(new_pass)}'
        print(f'{i} -> {new_pass} ({specs})')
    #print(string.punctuation)









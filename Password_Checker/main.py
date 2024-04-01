

def check_password(password: str):
    with open('Password_Checker/passwords.txt', 'r') as file:
        common_password: list[str] = file.read().splitlines()
    for i, common_password in enumerate(common_password, start=1):
        if password == common_password:
            print(f'{password}: ❌ (#{i})')
            return
        
    print(f'{password}: ✅ (Unique)')

def main():
    #? Checks if password is provided, stops user from using a empty string
    while True:
        user_password: str = input('Enter a password ')
        if user_password:
            break
        else:
            print('The password cannot be left blank. Please enter a password.')
    check_password(user_password)

if __name__ == '__main__':
    main()






def login(password, email):
    current__password = 'password'
    current__email = 'kike@gmail.com'

    # Validar Usuario
    if password == current__password and  email == current__email:
        return 'Ok'
    else:
        return 'Fail'

    

user = login('password', 'kike@gmail.com')

if user == 'Ok':
    print('Welcome')
else:
    print('Error')
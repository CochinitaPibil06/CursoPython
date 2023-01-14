def login(password, email):
    current__password = 123
    current__email = 'kike@gmail.com'

    # Validar Usuario
    if password == current__password and  email == current__email:
        return 'Ok'
    else:
        return 'Fail'


response = ""
try:
    password = int(input("Contraseña: "))
    email = input("Correo: ")
    response = login(password, email)
except NameError:
    # print(NameError)
    print('Error')
else:
    if response == 'Ok':
        print('Welcome')
    else:
        print("La contraseña o correo son incorrectos")
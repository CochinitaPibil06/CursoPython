# Funcion que si el numero que le envio es igual a mi numero favorito, me devolvera mi numero, sino, me dira que ese no es mi numero

# Funcion para validar si el numero que le envio, es mi numero favorito
def favoriteNumber(Num):
    
    # Este es mi numero favorito
    myNumber = 6

    # Validar si el numero es igual a mi numero favorito
    if  Num == myNumber:
        return 'si'

# Guardamos en una variable el valor que le devolvemos al llamar a nuestra funcion
numero = favoriteNumber(4)

# Validar si el valor que me devolvio mi funcion, es correcta
if numero == 'si':
    print('estas bien :v')
else:
    print('estas mal :,v')

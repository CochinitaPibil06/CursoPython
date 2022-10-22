def resta(num1, num2):
    print(num1 - num2)

def multiplicacion(num1, num2):
    print(num1 * num2)

def divicion(num1, num2):
    print(num1 / num2)

def suma(num1, num2):
    print(num1 + num2)

def AlCuadrado(num1):
    print(num1**2)

def AlCubo(num1):
    print(num1**3)

def Residuo(num1,num2):
    print(num1%num2)

#Inicio de bucle
while True:

    print("------ Menu ------")
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Elevar al cuadrado")
    print("6) Elevar al cubo")
    print("7) Residuo")
    print("8) Salir")
    print("--------------------")

    opcion = int(input("Escoge una opcion: "))

    if opcion == 8:
        break

    elif opcion == 5:
        num1 = int(input("Numero: "))
        AlCuadrado(num1)

    elif opcion == 6:
        num1 = int(input("Numero: "))
        AlCubo(num1)
    
    elif opcion == 7:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        Residuo(num1, num2)

    elif opcion == 1:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        suma(num1, num2)
    elif opcion == 2:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resta(num1, num2)
    elif opcion == 3:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        multiplicacion(num1, num2)
    elif opcion == 4:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        divicion(num1, num2)


#Fin de bucle
print("adios :v")
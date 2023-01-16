# <Inicia clase>
# <>
class Calculadora:

    # <Aqui se envian 2 numeros a restar>
    def resta(num1, num2):
        return num1-num2
        

    # <Aqui se envian 2 numeros a Multiplicarse>
    def multiplicacion(num1, num2):
        return num1*num2

    # <Aqui se envian 2 numeros a Dividir>
    def divicion(num1, num2):
        if num2 != 0:
            return num1 / num2
        else:
            return "Error"

    # <Aqui se envian 2 numeros a Sumar>
    def suma(num1, num2):
        return num1 + num2

    # <Aqui se envian 1 numero a elevarse Al Cuadrado>
    def AlCuadrado(num1):
        return num1**2

    # <Aqui se envian 1 numero a elevarse Al Cubo>
    def AlCubo(num1):
        return num1**3

    # <Aqui se envian 2 numeros a buscar su residuo>
    def Residuo(num1,num2): 
        if num2 != 0:
            return num1%num2
        else:
            return "Error"
    
# <Acaba clase>

# <Inicia codigo principal>
# <Aqui se muestra el Menu de la calculadora y sus distitas opciones>

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

    #calculadora = Calculadora()

    if opcion == 8:
        break

    elif opcion == 5:
        num1 = int(input("Numero: "))
        resultado = Calculadora.AlCuadrado(num1)
        print(num1, "**", "2", "=", resultado)

    elif opcion == 6:
        num1 = int(input("Numero: "))
        resultado = Calculadora.AlCubo(num1)
        print(num1, "**", "3", "=", resultado)

    elif opcion == 7:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resultado = Calculadora.Residuo(num1, num2)
        if resultado == "Error":
            print("No se puede dividir entre cero")
        else:
            print(num1, "%", num2, "=", resultado)

    elif opcion == 1:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resultado = Calculadora.suma(num1, num2)
        print(num1, "+", num2, "=", resultado)
    elif opcion == 2:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resultado = Calculadora.resta(num1, num2)
        print(num1, "-", num2, "=", resultado)
    elif opcion == 3:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resultado = Calculadora.multiplicacion(num1, num2)
        print(num1, "*", num2, "=", resultado)
    elif opcion == 4:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        resultado = Calculadora.divicion(num1, num2)
        if resultado == "Error":
            print("No se puede dividir entre cero")
        else:
            print(num1, "/", num2, "=", resultado)


# <Acaba codigo principal>
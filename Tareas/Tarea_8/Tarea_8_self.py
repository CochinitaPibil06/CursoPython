# <Inicia clase>
# <>
class Calculadora:

    def __init__(self, num1, num2=None):
        self.num1 = num1
        self.num2 = num2
        
    # <Aqui se envian 2 numeros a restar>
    def resta(self):
        return self.num1-self.num2
        

    # <Aqui se envian 2 numeros a Multiplicarse>
    def multiplicacion(self):
        return self.num1*self.num2

    # <Aqui se envian 2 numeros a Dividir>
    def divicion(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error"

    # <Aqui se envian 2 numeros a Sumar>
    def suma(self):
        return self.num1 + self.num2

    # <Aqui se envian 1 numero a elevarse Al Cuadrado>
    def AlCuadrado(self):
        return self.num1**2

    # <Aqui se envian 1 numero a elevarse Al Cubo>
    def AlCubo(self):
        return self.num1**3

    # <Aqui se envian 2 numeros a buscar su residuo>
    def Residuo(self):
        if self.num2 != 0:
            return self.num1 % self.num2
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


    if opcion == 8:
        break

    elif opcion == 5:
        num1 = int(input("Numero: "))
        calculadora = Calculadora(num1)
        resultado = calculadora.AlCuadrado()
        print(num1, "**", "2", "=", resultado)
    elif opcion == 6:
        num1 = int(input("Numero: "))
        calculadora = Calculadora(num1)
        resultado = calculadora.AlCubo()
        print(num1, "**", "3", "=", resultado)

    elif opcion == 7:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.Residuo()
        if resultado == "Error":
            print("No se puede dividir entre cero")
        else:
            print(num1, "%", num2, "=", resultado)
    elif opcion == 1:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.suma()
        print(num1, "+", num2, "=", resultado)
    elif opcion == 2:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.resta()
        print(num1, "-", num2, "=", resultado)
    elif opcion == 3:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.multiplicacion()
        print(num1, "*", num2, "=", resultado)
    elif opcion == 4:
        num1 = int(input("Numero1: "))
        num2 = int(input("Numero2: "))
        calculadora = Calculadora(num1, num2)
        resultado = calculadora.divicion()
        if resultado == "Error":
            print("No se puede dividir entre cero")
        else:
            print(num1, "/", num2, "=", resultado)

# <Acaba codigo principal>
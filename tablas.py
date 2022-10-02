#Tablas de multiplicar 

# Asignar un numero
num = int(input("Escribe un numero: "))

# Ciclo for
for index in range(10, 0, -1):
    print(num, "x", index, "=", num*index)
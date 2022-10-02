
# Break/terminar

# Asignar un numero
age = int(input("Escribe tu edad: "))
if age > 100:
    print("Esa edad ya esta murida papu :v")
else:

# Ciclo for
    for index2 in range(1, 101):
        if index2 == age:
            print("Tienes ", index2, "años")
            break
        print(index2)
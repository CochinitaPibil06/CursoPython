
# Break/terminar
def GetEdades(currentAge):
    # Ciclo for
    for age in range(1, 101):
        if age == currentAge:
            print("Tienes ", age, "años")
            break
        print(age)

# Asignar un numero
age = int(input("Escribe tu edad: "))
if age > 100:
    print("Esa edad ya esta murida papu :v")
else:   
    GetEdades(age)

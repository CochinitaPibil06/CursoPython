# Empezar bucle
def salir(valor):
    if valor == "salir":
        return True 
    else:
        return False



ciclo=True

while ciclo:
    # Obtener valor
    valor = input("Introduce algo: ")
    # Condicion: si el valor es igual a "salir", termina el bucle

# Otra manera de validar
#     validacion = salir(valor)
#    if validacion:
#         ciclo = False 


    if salir(valor):
        ciclo = False 
    else:
        print(valor)
# Fin del bucle
print("fin del codigo")
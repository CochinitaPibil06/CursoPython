# def semana(dia):
#  if dia == 1: 
#      print("lunes")
#  elif dia == 2: 
#      print("martes")
#  elif dia == 3:
#      print("miercoles")
#  elif dia == 4:
#      print("jueves")
#  elif dia == 5:
#      print("viernes")
#  elif dia == 6:
#      print("sabado")
#  elif dia == 7:
#      print("domingo")
#  else:
#      print("Este dia de la semana no existe")

# dia = int(input("Escribe un numero de la semana: "))
# semana(dia)
#Condicion: Si el numero es igual a un dia de la semana, Imprimira dicho dia, Sino, decirle al usuario que dicho dia no existe

def diaSemana(dia):
    if dia > (len(semana)-1):
        print("Este dia de la semana no existe")
    else:
        print(semana[dia - 1])
        

semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

dia = int(input("Escribe un numero de la semana: "))
diaSemana(dia)

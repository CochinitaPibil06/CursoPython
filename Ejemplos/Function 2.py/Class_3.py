import time 

class Vehiculo:
    def __init__(self, Salud, Velocidad):
        self.Salud = Salud
        self.Velocidad = Velocidad

    def __ValidacionVehiculo(self):

        valido = True

        if self.Salud < 102.4:
            print("La salud del vehiculo esta bajando... ¡Tenga cuidado!...")
            valido = False
        elif self.Salud > 102.4:
            print("Salud: Estable...")
            valido = False

        elif self.Velocidad < 32.6:
            print("Mas rapido Anciana/o...")
            valido = False
        elif self.Velocidad > 32.6:
            print("Le recomiendo ir a la velocidad acignada... No sea que choques...")
            valido = False

        return valido

    def __Preparado(self):
        self.__Moviendoce()
        self.__salud()

    def __Moviendoce(self):
        print("(moviendo)")
        time.sleep(1.2)

    def __salud(self):
        print("Salud: 100%")
        time.sleep(0.9)

    def Vehicul0(self):
        if self.__ValidacionVehiculo():
            self.__Preparado()
            print("Broom, Broom")
        else:
            print("¡Checa que todo este bien!")


Cochecito = Vehiculo(102.4, 32.6)
Cochecito.Vehicul0()
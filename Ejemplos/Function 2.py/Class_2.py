import time

class Personaje:
    def __init__(self, Vida, Escudo, CapacidadMunicion):
        self.Vida = Vida
        self.Escudo = Escudo
        self.CapacidadMunicion = CapacidadMunicion

    def __ValidacionDelPersonaje(self):

        valido = True

        if self.Vida < 100:
            print("Projura recuperar tu vida antes de que te mueras...")
            valido = False
        elif self.Vida > 100:
            print("(Tu vida ya esta al maximo...)")
            valido = False
            
        elif self.Escudo < 100:
            print("Projura recuperar algo Escudo antes de que te mueras...")
            valido = False
        elif self.Escudo > 100:
            print("(Tu Escudo ya esta al maximo...)")
            valido = False

        elif self.CapacidadMunicion < 57.9:
            print("Le recomiendo conseguir mas municion soldado...")
            valido = False
        elif self.CapacidadMunicion > 57.9:
            print("Tienes demasiada municion, comparte algo...")
            valido = False

        return valido

    def __Preparacion(self):
        self.__Recuperando()
        self.__Escudos()
        self.__Municiones()

    def __Recuperando(self):
        print("Salud:+100%")
        time.sleep(3.6)

    def __Escudos(self):
        print("Escudo:[IIXXXXXXXX] 20%")
        time.sleep(2)
        print("Escudo:[IIIXXXXXXX] 30%")
        time.sleep(2)
        print("Escudo:[IIIIXXXXXX] 40%")
        time.sleep(2)
        print("Escudo:[IIIIIXXXXX] 50%")
        time.sleep(2)
        print("Escudo:[IIIIIIIIII] 100%")
        time.sleep(2)

    def __Municiones(self):
        print("Municion:FULL")
        time.sleep(1.8)


    def Listo(self):
        if self.__ValidacionDelPersonaje():
            self.__Preparacion()
            print("Es hora de partir soldado")
        else:
            print("¡Ups!... Checa que todo este listo antes de partir")

    
FormandoPersonaje = Personaje(100, 100, 57.9)
FormandoPersonaje.Listo()

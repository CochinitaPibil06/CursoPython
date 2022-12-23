import time

class Galleta:
    
    # Asignar los ingredientes
    def __init__(self, mantequilla, lechera, vainilla, huevo, harina, polvoHornear):
        self.mantequilla = mantequilla
        self.lechera = lechera
        self.vainilla = vainilla
        self.huevo = huevo
        self.harina = harina
        self.polvoHornear = polvoHornear

    # Validar ingredientes
    def __validarIngredientes(self):

        valido = True
        
        # Validar mantequilla
        if self.mantequilla < 0.5:
            print("Esa cantidad no es la indicada, te falta mantequilla")
            valido = False
        elif self.mantequilla > 0.5:
            print("Esa cantidad no es la indicada, te pasaste de mantequilla")
            valido = False

        # Validar lechera
        if self.lechera < 387:
            print("Esa cantidad no es la indicada, te falta lechera")
            valido = False
        elif self.lechera > 387:
            print("Esa cantidad no es la indicada, te pasaste de lechera")
            valido = False

        # Validar vainilla
        if self.vainilla < 15:
            print("Esa cantidad no es la indicada, te falta vainilla")
            valido = False
        elif self.vainilla > 15:
            print("Esa cantidad no es la indicada, te pasaste de vainilla")
            valido = False

        # Validar huevo
        if self.huevo < 1:
            print("Esa cantidad no es la indicada, te falta huevo")
            valido = False
        elif self.huevo > 1:
            print("Esa cantidad no es la indicada, te pasaste de huevo")
            valido = False
            
        # Validar harina
        if self.harina < 195:
            print("Esa cantidad no es la indicada, te falta harina")
            valido = False
        elif self.harina > 195:
            print("Esa cantidad no es la indicada, te pasaste de harina")
            valido = False
            
        # Validar polvo para hornear
        if self.polvoHornear < 12.5:
            print("Esa cantidad no es la indicada, te falta polvo para hornear")
            valido = False
        elif self.polvoHornear > 12.5:
            print("Esa cantidad no es la indicada, te pasaste de polvo para hornear")
            valido = False

        return valido
            
    # Preparar masa para galletas
    def __preparar(self):
            self.__mezclar()
            self.__hornear()            
        
    def __mezclar(self):
        print("Mezclando...")
        time.sleep(2)
        
    #Hornear galleta
    def __hornear(self):
        print("Horneando...")
        time.sleep(4)

    # Crear nueva galleta
    def nueva(self):
        if self.__validarIngredientes():
            self.__preparar()
            print("Ten tu nueva galleta")
        else:
            print("¡Ups!, checa bien tus ingredientes")


galletaObjeto = Galleta(0.5, 387, 15, 1, 195, 12.5)
galletaObjeto.nueva()


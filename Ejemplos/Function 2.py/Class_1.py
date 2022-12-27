import time

class Arma:
    def __init__(self, CantidadDeBalas, Recargar):
        self.CantidadDeBalas = CantidadDeBalas
        self.Recargar = Recargar

    def __ValidarArma(self):

        Valido = True

        if self.CantidadDeBalas < 12:
            print("Esa cantidad de balas es muy poca, projure tener mas")
            Valido = False
        elif self.CantidadDeBalas > 12:
            print("Tu arma ya tiene las balas suficientes")
            Valido = False

        elif self.Recargar < 12:
            print("Esa cantidad de balas es muy poca, projure tener mas")
            Valido = False

        elif self.Recargar > 12:
            print("Tu arma ya esta recargada")
            Valido = False

        return Valido

    def __recarga(self):
        self.__Recargar()


    def __Recargar(self):
        print("Recargando...")
        time.sleep(2)

    def Disparo(self):
        if self.__ValidarArma():
            self.__recarga()
            print("piu..piu")
        else:
            print("(O no... Checa que la canidad de balas sean las indicadas)")
    
      


ArmaObjeto = Arma(14, 12)
ArmaObjeto.Disparo()
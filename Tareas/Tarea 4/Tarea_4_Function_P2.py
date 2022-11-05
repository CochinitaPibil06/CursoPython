def Obciones(TipoDeCamisa, TallaDeCamisa):
    camisa = 'azulj'
    talla = 13

    if TipoDeCamisa == camisa and TallaDeCamisa == talla:
        return 'si'
    else:
        return 'no'

Cliente = Obciones('azul', 13)

if Cliente == 'si':
    print("Esto es lo que necesitaba")
else:
    print("Esto no es lo que quiero >:v")
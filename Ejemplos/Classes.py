class MyClass:
  myPdroperty = 5

myObject = MyClass()
#print(myObject.myPdroperty)




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

person = Person("John", 36)

#print(type(person))

#print(person.name)
#print(person.age)


class RecetaGalleta:
    mantequilla = 0.5
    lechera = 387
    vainilla = 15
    huevo = 1
    harina = 195
    polvoHornear = 12.5
    chispas = 195

receta = RecetaGalleta()

#print(receta.lechera)

class Galleta:
    def __init__(self, mantequilla, lechera, vainilla, huevo, harina, polvoHornear, chispas):
        self.mantequilla = mantequilla
        self.lechera = lechera
        self.vainilla = vainilla
        self.huevo = huevo
        self.harina = harina
        self.polvoHornear = polvoHornear
        self.chispas = chispas

galleta = Galleta(0.5, 187, 15, 1, 195, 12.5, 195)
#print(galleta.chispas)


class Person2:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"Mi nombre es {self.name} y tengo {self.age} años"

p1 = Person2("John", 36)

#print(p1)


class Person3:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person3("John", 36)
p1.myfunc()
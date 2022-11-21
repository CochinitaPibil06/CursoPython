
#funcion
def numero(num1):
    #iclo for
  for num in range(1, 11):
    print(num1, "x", num, "=", num1*num)

def main():
  num1 = int(input("Escribe un numero: "))
  numero(num1)


if __name__ == "__main__":
    main()
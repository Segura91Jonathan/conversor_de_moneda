# print(2**0)
# print(2**1)
# print(2**2)
# print(2**3)
# print(2**4)
# print(2**5)
# print(2**6)
# print(2**7)
# print(2**8)
# print(2**9)
# print(2**10)

def run():
    LIMITE = 1000000
    contador = 0
    potencia_2 = 2**contador

    while potencia_2 < LIMITE:
        print("2 elevado a "+str(contador)+ " es igual a: "+ str(potencia_2))
        contador = contador + 1
        potencia_2 = 2 ** contador


if __name__ == "__main__":
    run()
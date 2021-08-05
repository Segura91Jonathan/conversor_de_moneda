def factorial(numero):
#numero = int(input("ingrese un numero:"))
    
    contador = 1
    total =1

    while contador < numero :
        contador += 1
        total = total * contador

    return total

def es_primo(numero):
    if (factorial(numero-1)+1) % numero == 0:
        return True
    else:
        return False


def run():
    numero = int(input("ingrese un numero: "))
    if es_primo(numero):
        print("es primo")
    else:
        print("no es primo")


if __name__ == "__main__":
    run()
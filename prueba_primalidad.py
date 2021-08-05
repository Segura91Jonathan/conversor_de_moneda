def es_primo(numero):
    contador = 0

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
    
    if contador == 0:
        return True
    else:
        return False


def run():
    # contador = 1

    # for contador in range(101):
    #     if contador % contador == 0 and contador % 1 == 0:
    #         print("el numero primo es : " + str(contador))
    #         contador += 1
    #     else:
    #         print(contador)
    #         contador +=1


    # number = int(input("ingrese un numero"))

    # if es_primo(number):
    #     print("es primo")
    # else:
    #     print("no es primo")


    contador = 1

    for contador in range(101):
         if es_primo(contador):
             print("el numero : " + str(contador)+" es primo")
             contador += 1
         else:
             print(contador)
             contador +=1



if __name__ == "__main__":
    run()
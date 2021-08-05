def run():
    
    contador = 1

    while contador < 1000:

        if contador % 2 == 0:
            print("el contador con el valor: " + str(contador)+" es un numero par")
            contador +=1
            continue
        else:
            if contador < 560:
                print(contador)
                contador +=1
            else:
                print("ultimo valor antes del limite interno que es: "+ str(contador))
                contador -=1
                print(contador)
                break
                



if __name__ == "__main__":
    run()
def run():
    mi_diccionario = {
        "key1" : 1,
        "key2" : 2,
        "key3" : 3,
    }

    # print(mi_diccionario)
    # print(mi_diccionario["key1"])


    poblacion_paises = {
        "argeintina" :  45000000,
        "china" : 1000000000,
        "colombia" :50372424,
    }

    # print(poblacion_paises["maiami"])

    # for pais in poblacion_paises.values():
    #     print(pais)

    # for pais in poblacion_paises.keys():
    #     print(pais)

    for pais in poblacion_paises.items():
        print(pais)

if __name__ == "__main__":
    run()
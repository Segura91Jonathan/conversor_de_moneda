menu = """

Welcome to currency converter:

1- pesos argentinos
2- pesos uruguayos
3- pesos mexicanos

please choose an option:

"""

opcion = int(input(menu))

if opcion == 1:
    pesos = input("cuantos pesos argentinos tenes? :")
    pesos = float(pesos)
    valor_dolar = 190
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tenes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("cuantos pesos uruguayos tenes? :")
    pesos = float(pesos)
    valor_dolar = 43.59
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tenes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("cuantos pesos mexicanos tenes? :")
    pesos = float(pesos)
    valor_dolar = 19.98
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tenes $" + dolares + " dolares")
else:
     print("ingrese una opcion correcta")




# dolares1 = input("ingrese su cantidad de dolares: ")
# dolares1 = float(dolares1)
# valor_peso = 190
# pesos1 = dolares1 * valor_peso
# pesos1 = round(pesos1,2)
# pesos1 = str(pesos1)
# print("tenes $" + pesos1 + " pesos")


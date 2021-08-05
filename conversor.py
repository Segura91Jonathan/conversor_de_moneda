def conversor(tipo_pesos,valor_dolar):
    pesos = input("cuantos pesos " +tipo_pesos +" tenes? :")
    pesos = float(pesos)
    #valor_dolar = 190
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares = str(dolares)
    print("tenes $" + dolares + " dolares")

menu = """

Welcome to currency converter:

1- pesos argentinos
2- pesos uruguayos
3- pesos mexicanos

please choose an option:

"""

opcion = int(input(menu))

if opcion == 1:
    
    conversor("argentinos",190)
elif opcion == 2:
    
    conversor("uruguayos",43.59)
elif opcion == 3:

    conversor("mexicanos",19.98)
else:
     print("ingrese una opcion correcta")




# dolares1 = input("ingrese su cantidad de dolares: ")
# dolares1 = float(dolares1)
# valor_peso = 190
# pesos1 = dolares1 * valor_peso
# pesos1 = round(pesos1,2)
# pesos1 = str(pesos1)
# print("tenes $" + pesos1 + " pesos")


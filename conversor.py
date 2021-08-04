pesos = input("cuantos pesos tenes? :")
pesos = float(pesos)
valor_dolar = 190
dolares = pesos / valor_dolar
dolares = round(dolares,2)
dolares = str(dolares)
print("tenes $" + dolares + " dolares")
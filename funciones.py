# def imprimir_mensaje():
#     print("mensaje especial")
#     print("learning how to use functions")


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def conversation(mensaje):
    print("Hello")
    print("HOw r U")
    print(mensaje)
    print("bye")


opcion = int(input("ingrese una opcion(1,2,3):"))



if opcion == 1:
    # print("Hello")
    # print("HOw r U")
    # print("U choose opcion 1")
    # print("bye")
    conversation("Elegiste el valor 1")
elif opcion == 2:
    # print("Hello")
    # print("HOw r U")
    # print("U choose opcion 2")
    # print("bye")
    conversation("Elegiste el valor 2")
elif opcion == 3:
    # print("Hello")
    # print("HOw r U")
    # print("U choose opcion 3")
    # print("bye")
    conversation("Elegiste el valor 3")
else:
    print("please choose a correct option")
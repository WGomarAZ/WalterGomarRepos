def insertar_inicio():
    dato = input("Ingrese un dato: ")
    print("se ha insertado el dato: "+dato+" al inicio de la lista")

def insertar_final():
    dato = input("Ingrese un dato: ")
    print("se ha insertado el dato: "+dato+" al final de la lista")

def eliminar_por_valor():
    dato = input("Ingrese un dato: ")
    print("se ha eliminado el dato: "+dato+" de ña lista")

def mostrar_lista():
    print("elementos de la lista doblemente enlazada")

def Salir():
    exit()

def invalido():
    print("opcion no válida, ingrese un número del 1 al 5")

while True:
    print("Menu de operaciones: lista doblemente enlazada")
    print("1. Insertar al inicio de la lista")
    print("2. Insertar al final de la lista")
    print("3. Elimnar de la lista un valor específico")
    print("4. Mostar lista")
    print("5. Salir del programa")
    valor = input("Seleccione una opcion: ")
    if(valor == "1"):
        insertar_inicio()
        continuar = input("Presione ENTER para continuar: ")
    elif(valor == "2"):
        insertar_final()
        continuar = input("Presione ENTER para continuar: ")
    elif(valor == "3"):
        eliminar_por_valor()
        continuar = input("Presione ENTER para continuar: ")
    elif(valor == "4"):
        mostrar_lista()
        continuar = input("Presione ENTER para continuar: ")
    elif(valor == "5"):
        Salir()
    else: invalido()
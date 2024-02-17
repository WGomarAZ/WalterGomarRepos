import msvcrt
import os


class Nodo:
    def __init__(self, nombre, apellido, carnet):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None


class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def carnet_repetido(self, carnet):
        nodo_actual = self.cabeza
        while (nodo_actual):
            if (nodo_actual.carnet == carnet):
                return True
            nodo_actual = nodo_actual.siguiente
        return False

    def insertar_al_inicio(self, nombre, apellido, carnet):
        if (self.carnet_repetido(carnet)):
            return True

        nuevo_nodo = Nodo(nombre, apellido, carnet)
        nuevo_nodo.siguiente = self.cabeza
        nuevo_nodo.anterior = None
        if (self.cabeza is not None):
            self.cabeza.anterior = nuevo_nodo
        self.cabeza = nuevo_nodo
        if (self.cola is None):
            self.cola = nuevo_nodo

    def insertar_al_final(self, nombre, apellido, carnet):
        if (self.carnet_repetido(carnet)):
            return True

        nuevo_nodo = Nodo(nombre, apellido, carnet)
        nuevo_nodo.anterior = self.cola
        nuevo_nodo.siguiente = None
        if (self.cola is not None):
            self.cola.siguiente = nuevo_nodo
        self.cola = nuevo_nodo
        if (self.cabeza is None):
            self.cabeza = nuevo_nodo

    def eliminar_por_valor(self, carnet):
        if (self.cabeza is None and self.cola is None):
            print("Lista vacia, primero debe ingresar datos.")
            return

        nuevo_nodo = self.cabeza
        while (nuevo_nodo):
            if (nuevo_nodo.carnet == carnet and nuevo_nodo.siguiente == None and nuevo_nodo.anterior == None):
                self.cabeza = None
                self.cola = None
                nuevo_nodo = None
                print("El registro fue eliminado correctamente.")
                break

            elif (nuevo_nodo.anterior == None and nuevo_nodo.carnet == carnet):
                nuevo_nodo = nuevo_nodo.siguiente
                nuevo_nodo.anterior = None
                self.cabeza = nuevo_nodo
                print("El registro fue eliminado correctamente.")
                break

            elif (nuevo_nodo.siguiente == None and nuevo_nodo.carnet == carnet):
                nuevo_nodo = nuevo_nodo.anterior
                nuevo_nodo.siguiente = None
                self.cola = nuevo_nodo
                print("El registro fue eliminado correctamente.")
                break

            else:
                if (nuevo_nodo.carnet == carnet):
                    nodo_temporal_uno = nuevo_nodo.anterior
                    nodo_temporal_dos = nuevo_nodo.siguiente
                    nodo_temporal_uno.siguiente = nodo_temporal_dos
                    nodo_temporal_dos.anterior = nodo_temporal_uno
                    nuevo_nodo = nodo_temporal_dos
                    print("El registro fue eliminado correctamente.")
                    break

                elif (nuevo_nodo.siguiente == None and nuevo_nodo.carnet != carnet):
                    print("No se encontro el carnet que busca.")
                    break

                else:
                    nuevo_nodo = nuevo_nodo.siguiente

    def mostrar_datos(self):
        nuevo_nodo = self.cabeza
        literal = "None <- "
        while (nuevo_nodo):
            nodo_datos = f"{
                nuevo_nodo.carnet}: {nuevo_nodo.nombre} {nuevo_nodo.apellido}"
            if (nuevo_nodo.siguiente == None):
                literal += str(nodo_datos) + " -> "
            else:
                literal += str(nodo_datos) + " <-> "
            nuevo_nodo = nuevo_nodo.siguiente
        literal += "None"
        print(literal)


alumno = ListaDoblementeEnlazada()


def insertar_inicio():
    os.system("cls")
    print("Ingresando un alumno al inicio de la lista\n")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    carnet = int(input("Ingrese el número de carné del alumno: "))
    resultado = alumno.insertar_al_inicio(nombre, apellido, carnet)
    if (resultado):
        os.system("cls")
        print("Número de carné repetido, ingrese uno diferente")
    else:
        os.system("cls")
        print(f"""Se registró con éxito la siguiente información: {
              carnet} - {nombre} {apellido}""")
    print("\nPresione ENTER para continuar...")
    msvcrt.getch()


def insertar_final():
    os.system("cls")
    print("Ingresando un alumno al final de la lista\n")
    nombre = input("Ingrese el nombre del alumno: ")
    apellido = input("Ingrese el apellido del alumno: ")
    carnet = int(input("Ingrese el número de carné del alumno: "))
    resultado = alumno.insertar_al_final(nombre, apellido, carnet)
    if (resultado):
        os.system("cls")
        print("Número de carné repetido, ingrese uno diferente")
    else:
        os.system("cls")
        print(f"""Se registró con éxito la siguiente información: {
              carnet} - {nombre} {apellido}""")
    print("\nPresione ENTER para continuar...")
    msvcrt.getch()


def mostrar_lista():
    os.system("cls")
    print("elementos de la lista doblemente enlazada")
    print("Presione ENTER para continuar...")
    msvcrt.getch()


def eliminar_por_valor():
    os.system("cls")
    print("Eliminar alumno de la lista\n")
    carnet = int(input("Ingrese el carné del alumno que desea eliminar: "))
    alumno.eliminar_por_valor(carnet)
    print("\nPresione ENTER para continuar...")
    msvcrt.getch()


def Salir():
    os.system("cls")
    print("Saliendo del programa, presione cualquier tecla pra continuar...")
    msvcrt.getch()
    exit()


def invalido():
    os.system("cls")
    print("Opcion no válida, ingrese un número del 1 al 5...")
    msvcrt.getch()


while True:
    os.system("cls")
    print("Menu de operaciones: lista doblemente enlazada")
    print("1. Insertar al inicio de la lista")
    print("2. Insertar al final de la lista")
    print("3. Mostar lista")
    print("4. Elimnar de la lista un valor específico")
    print("5. Salir del programa")
    valor = input("Seleccione una opcion: ")
    if (valor == "1"):
        insertar_inicio()
    elif (valor == "2"):
        insertar_final()
    elif (valor == "3"):
        mostrar_lista()
    elif (valor == "4"):
        eliminar_por_valor()
    elif (valor == "5"):
        Salir()
    else:
        invalido()

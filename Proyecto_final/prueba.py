import tkinter
from tkinter import messagebox
import random
from graph import GrafoTotito  # Asegúrate de que el nombre del archivo sea correcto


class Totito:
    def __init__(self, root):
        self.root = root
        self.root.title("Totito")
        self.turno = "X"
        self.tablero = {"A1": "", "A2": "", "A3": "", "B1": "", "B2": "", "B3": "", "C1": "", "C2": "", "C3": ""}
        self.botones = {}
        self.grafo = GrafoTotito()

        self.crear_tablero()

    def crear_tablero(self):
        posiciones = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]
        fil = 0
        col = 0
        for posicion in posiciones:
            boton = tkinter.Button(
                self.root,
                text="",
                font=("normal", 40),
                width=5,
                height=2,
                command=lambda pos=posicion: self.control_clics(pos),
            )
            boton.grid(row=fil, column=col)
            self.botones[posicion] = boton
            col += 1
            if col > 2:
                col = 0
                fil += 1

    def control_clics(self, pos):
        if self.tablero[pos] == "" and self.verificar_ganador() is None:
            self.tablero[pos] = self.turno
            self.botones[pos].config(text=self.turno)

            estado_actual = self.obtener_estado()
            self.grafo.agregar_estado(estado_actual)

            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"{self.turno} gana.")
                self.grafo.actualizar_valores_q(self.turno, "victoria")
                self.limpiar_tablero()
            elif all(valor != "" for valor in self.tablero.values()):
                messagebox.showinfo("Fin del juego", "Empate.")
                self.grafo.actualizar_valores_q(self.turno, "empate")
                self.limpiar_tablero()
            else:
                self.turno = "O"
                self.turno_maquina()

    def turno_maquina(self):
        movimientos_disponibles = [k for k, v in self.tablero.items() if v == ""]
        estado_actual = self.obtener_estado()
        self.grafo.agregar_estado(estado_actual)

        movimiento = self.grafo.mejor_movimiento(estado_actual, movimientos_disponibles)

        if movimiento is not None:
            self.tablero[movimiento] = self.turno
            self.botones[movimiento].config(text=self.turno)

            estado_actual = self.obtener_estado()
            self.grafo.agregar_estado(estado_actual)

            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"{self.turno} gana.")
                self.grafo.actualizar_valores_q(self.turno, "victoria")
                self.limpiar_tablero()
            elif all(valor != "" for valor in self.tablero.values()):
                messagebox.showinfo("Fin del juego", "Empate")
                self.grafo.actualizar_valores_q(self.turno, "empate")
                self.limpiar_tablero()
            else:
                self.turno = "X"

    def obtener_estado(self):
        return tuple(self.tablero.values())

    def verificar_ganador(self):
        combinaciones = [
            ["A1", "A2", "A3"],  # Horizontales
            ["B1", "B2", "B3"],
            ["C1", "C2", "C3"],
            ["A1", "B1", "C1"],  # Verticales
            ["A2", "B2", "C2"],
            ["A3", "B3", "C3"],
            ["A1", "B2", "C3"],  # Diagonales
            ["A3", "B2", "C1"],
        ]

        for combinacion in combinaciones:
            if self.tablero[combinacion[0]] == self.tablero[combinacion[1]] == self.tablero[combinacion[2]] != "":
                return self.tablero[combinacion[0]]
        return None

    def limpiar_tablero(self):
        self.tablero = {"A1": "", "A2": "", "A3": "", "B1": "", "B2": "", "B3": "", "C1": "", "C2": "", "C3": ""}
        for boton in self.botones.values():
            boton.config(text="")
        self.turno = "X"
        self.grafo.reiniciar_historial_estados()


def ejecutar():
    root = tkinter.Tk()
    game = Totito(root)
    root.mainloop()


if __name__ == "__main__":
    ejecutar()

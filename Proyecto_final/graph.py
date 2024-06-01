import random


class GrafoTotito:
    def __init__(self):
        self.grafo = {}
        self.valores_q = {}
        self.historial_estado = []
        self.alpha = 0.1
        self.gamma = 0.9

    def agregar_estado(self, estado):
        if estado not in self.grafo:
            self.grafo[estado] = []
            self.valores_q[estado] = {}
            for movimiento in range(len(estado)):
                if estado[movimiento] == "":
                    self.valores_q[estado][movimiento] = 1

        self.actualizar_conexiones(estado)
        self.historial_estado.append(estado)

    def actualizar_conexiones(self, estado):
        for i in range(len(estado)):
            if estado[i] == "":
                nuevo_estado = list(estado)
                nuevo_estado[i] = "X" if estado.count("X") <= estado.count("O") else "O"
                nuevo_estado_tupla = tuple(nuevo_estado)

                if nuevo_estado_tupla not in self.grafo:
                    self.grafo[nuevo_estado_tupla] = []
                    self.valores_q[nuevo_estado_tupla] = {}
                    for movimiento in range(len(nuevo_estado_tupla)):
                        if nuevo_estado_tupla[movimiento] == "":
                            self.valores_q[nuevo_estado_tupla][movimiento] = 1

                if nuevo_estado_tupla not in self.grafo[estado]:
                    self.grafo[estado].append(nuevo_estado_tupla)
                if estado not in self.grafo[nuevo_estado_tupla]:
                    self.grafo[nuevo_estado_tupla].append(estado)

    def mejor_movimiento(self, estado, movimientos_disponibles):
        estado_str = str(estado)
        if estado_str not in self.valores_q:
            self.agregar_estado(estado_str)  # Asegurarse de que el estado esté en los valores Q

        if random.uniform(0, 1) < 0.1:
            return random.choice(movimientos_disponibles)
        else:
            estado_valores_q = self.valores_q[estado_str]
            valor_q_maximo = max(estado_valores_q[movimiento] for movimiento in movimientos_disponibles)
            mejores_movimientos = [
                movimiento
                for movimiento in movimientos_disponibles
                if estado_valores_q.get(movimiento, 0) == valor_q_maximo
            ]
            return random.choice(mejores_movimientos)

    def actualizar_valores_q(self, turno, resultado):
        recompensa = 0
        if resultado == "victoria":
            recompensa = 1 if turno == "O" else -1
        elif resultado == "empate":
            recompensa = 0.5

        for i in range(len(self.historial_estado) - 1, -1, -1):
            estado = self.historial_estado[i]
            if i == len(self.historial_estado) - 1:
                recompensa_futura = recompensa
            else:
                proximo_estado = self.historial_estado[i + 1]
                recompensa_futura = self.gamma * max(self.valores_q[proximo_estado].values())

            if i == 0:
                movimiento = [
                    indice for indice in range(len(estado)) if self.historial_estado[i + 1][indice] != estado[indice]
                ][0]
            else:
                movimiento = [
                    indice
                    for indice in range(len(estado))
                    if self.historial_estado[i][indice] != self.historial_estado[i - 1][indice]
                ][0]

            self.valores_q[estado][movimiento] = (1 - self.alpha) * self.valores_q[estado][
                movimiento
            ] + self.alpha * recompensa_futura

    def reiniciar_historial_estados(self):
        self.historial_estado = []

    def is_winner(self, estado):
        combinaciones = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Filas
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Columnas
            [0, 4, 8],
            [2, 4, 6],  # Diagonales
        ]

        for combinacion in combinaciones:
            if estado[combinacion[0]] == estado[combinacion[1]] == estado[combinacion[2]] != "":
                return True
        return False

import tkinter as tk
import random

# ---------------------------------------------------------------
# VENTANA PRINCIPAL
# ---------------------------------------------------------------
ventana = tk.Tk()
ventana.title("Tic Tac Toe - Simple con Menú")

# ---------------------------------------------------------------
# VARIABLES GLOBALES
# ---------------------------------------------------------------
tablero = [" " for _ in range(9)]   # Guarda las 9 casillas
botones = []                        # Guarda los botones del tablero
modo = None                         # "hvh" = humano vs humano, "hvc" = humano vs compu
turno = "X"                         # X juega primero


# ---------------------------------------------------------------
# FUNCIONES DEL MENÚ
# ---------------------------------------------------------------
def elegir_hvh():
    """Selecciona el modo Humano vs Humano"""
    global modo
    modo = "hvh"
    mostrar_tablero()


def elegir_hvc():
    """Selecciona el modo Humano vs Computadora"""
    global modo
    modo = "hvc"
    mostrar_tablero()


def mostrar_menu():
    """Muestra la pantalla inicial con las opciones del juego"""
    titulo = tk.Label(ventana, text="Tic Tac Toe", font=("Arial", 22))
    titulo.pack(pady=20)

    # Botón para jugar Humano vs Humano
    b1 = tk.Button(ventana, text="Humano vs Humano",
                   font=("Arial", 18), width=20, command=elegir_hvh)
    b1.pack(pady=10)

    # Botón para jugar Humano vs Computadora
    b2 = tk.Button(ventana, text="Humano vs Computadora",
                   font=("Arial", 18), width=20, command=elegir_hvc)
    b2.pack(pady=10)


# ---------------------------------------------------------------
# CREAR TABLERO
# ---------------------------------------------------------------
def mostrar_tablero():
    """Crea los 9 botones del tablero y reinicia el juego"""
    # Limpia la pantalla (borra el menú)
    for widget in ventana.winfo_children():
        widget.destroy()

    global botones
    botones = []

    # Crear los botones del tablero (9 botones)
    for i in range(9):
        b = tk.Button(
            ventana,
            text=" ",
            font=("Arial", 32),
            width=5,
            height=2,
            command=lambda x=i: presionar(x)   # Cada botón tiene su posición
        )
        b.grid(row=i // 3, column=i % 3)
        botones.append(b)

    reiniciar_tablero()


def reiniciar_tablero():
    """Reinicia las variables del juego"""
    global tablero, turno
    tablero = [" " for _ in range(9)]
    turno = "X"

    for b in botones:
        b["text"] = " "


# ---------------------------------------------------------------
# LÓGICA DEL JUEGO
# ---------------------------------------------------------------
def presionar(pos):
    """Acción cuando el jugador presiona una casilla"""
    global turno

    # Si la casilla ya tiene algo, no se puede jugar ahí
    if tablero[pos] != " ":
        return

    # Marcar el movimiento del jugador (X u O)
    tablero[pos] = turno
    botones[pos]["text"] = turno

    # Revisar si el jugador actual ganó
    if hay_ganador(turno):
        terminar(f"Ganó {turno}")
        return

    # Revisar empate
    if " " not in tablero:
        terminar("Empate")
        return

    # Cambiar turno
    turno = "O" if turno == "X" else "X"

    # Si el modo es humano vs computadora y es turno de O (computadora)
    if modo == "hvc" and turno == "O":
        ventana.after(400, turno_computadora)


def turno_computadora():
    """Movimiento aleatorio de la computadora"""
    global turno

    # Buscar posiciones vacías
    vacias = []
    for i in range(9):
        if tablero[i] == " ":
            vacias.append(i)

    # Elegir una casilla al azar
    pos = random.choice(vacias)
    tablero[pos] = "O"
    botones[pos]["text"] = "O"

    # Revisar si la computadora ganó
    if hay_ganador("O"):
        terminar("La computadora ganó")
        return

    # Revisar empate
    if " " not in tablero:
        terminar("Empate")
        return

    # Regresar turno al jugador
    turno = "X"


def hay_ganador(j):
    """Comprueba si X u O ganó"""
    combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],   # filas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],   # columnas
        [0, 4, 8], [2, 4, 6]               # diagonales
    ]

    for c in combos:
        if tablero[c[0]] == j and tablero[c[1]] == j and tablero[c[2]] == j:
            return True
    return False


# ---------------------------------------------------------------
# FINAL DEL JUEGO
# ---------------------------------------------------------------
def terminar(mensaje):
    """Abre una ventana indicando quién ganó o si fue empate"""
    ventana2 = tk.Toplevel()
    ventana2.title("Fin del juego")

    tk.Label(ventana2, text=mensaje, font=("Arial", 20)).pack(pady=10)

    tk.Button(
        ventana2, text="Reiniciar",
        command=lambda: [ventana2.destroy(), mostrar_tablero()]
    ).pack(pady=5)

    tk.Button(ventana2, text="Cerrar juego", command=ventana.destroy).pack(pady=5)


# ---------------------------------------------------------------
# INICIO DEL PROGRAMA
# ---------------------------------------------------------------
mostrar_menu()
ventana.mainloop()
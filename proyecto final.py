#importaciones
import tkinter as tk
from tkinter import messagebox 
import random
#creamos nuestra ventana principal y le damos un nombre
ventana = tk.tk()
ventana.title ("mi proyecto final (juego de gato)")
tablero = ["" for _ in range (9)]
botones = []# para guardar los botones graficos
modo_Juego = None #para elegir si es humano vs humano o se quiere jugar con la computadora
turno = "X"

def Elegir_HvH():
    global modo_Juego
    modo_Juego = "humano VS humano"
    mostrar_Tablero()
def Elegir_hvc():
    global modo_Juego
    modo_Juego = "humano VS computadora"
    mostrar_Tablero()
    
def mostrar_menu():
    titulo = tk.label(ventana, text="juego de gato", font=("Arial", 22))
    titulo.pack(pady=20)
    
    b1 = tk.Button(ventana, text="Humano VS Humano", font=("Arial", 18),
                   width=20, command=elegir_hvh)
    b1.pack(pady=10)
    b2 = tk.Button(ventana, text= "Humano VS Computadora", font=("Arial", 18),
                   width=20, command=elegir_hvc)
    b2.pack(pady=10)
def mostrar_tablero():
    for widget in ventana.winfo_children():
        widget.destroy()
    global botones
    botones = []

    for i in range(9):
        b = tk.Button(
            ventana, text=" ", font=("Arial", 32),
            width=5, height=2,
            comand=lambda x=i: presionar(x)
        )
        b.grid(row=i // 3, column=i % 3)
        botones.append(b)

    reiniciar_Tablero()

def reiniciar_Tablero():
    global tablero, turno
    tablero = [" "for _ in range(9)]
    turno="X"
    for b in botones:
        b["text"] = ""

def presionar(pos):
    global turno
    if tablero[pos] !="":
        return
    tablero[pos] = turno
    botones[pos]["texto"] = turno
    
    if hay_ganador(turno):
        terminar(f"gano {turno}")
        return
    
    if "" not in tablero:
        terminar("empate")
        return
    turno = "O" if turno == "X" else "x"
    if modo == "hvc" and turno == "O":
        ventana.after(400, turno_computadora)
def turno_computadora():
def hay_ganador(j):
def otra_Partida():
def terminar(mensaje):
def nivel_Dificulad():


mostrar_menu
ventana. mainloop()
    

    



        
            
    






import tkinter as tk
from tkinter import messagebox

figuraActual = "circulo"
colorActual = "black"
anchoCanvas = 420
altoCanvas = 320
radio = 30

entradaX = None
entradaY = None
entradaNombre = None
etiquetaEstado = None
etiquetaSaludo = None
lienzo = None


def actualizarEstado():
    texto = "Figura: {} | Color: {}".format(figuraActual.capitalize(), colorActual)
    etiquetaEstado.config(text=texto)

def leerEntero(widget, predeterminado):
    texto = widget.get().strip()
    if texto == "":
        return predeterminado
    try:
        return int(texto)
    except ValueError:
        return predeterminado

def centroCanvas():
    return anchoCanvas // 2, altoCanvas // 2

def selCirculo():
    global figuraActual
    figuraActual = "circulo"
    actualizarEstado()

def selCuadrado():
    global figuraActual
    figuraActual = "cuadrado"
    actualizarEstado()

def selTriangulo():
    global figuraActual
    figuraActual = "triangulo"
    actualizarEstado()

def colNegro():
    global colorActual
    colorActual = "black"
    actualizarEstado()

def colRojo():
    global colorActual
    colorActual = "red"
    actualizarEstado()

def colMorado():
    global colorActual
    colorActual = "purple"
    actualizarEstado

def colAzul():
    global colorActual
    colorActual = "blue"
    actualizarEstado()

def colVerde():
    global colorActual
    colorActual = "green"
    actualizarEstado()

def dibujar():
    cx, cy = centroCanvas()
    x = leerEntero(entradaX, cx)
    y = leerEntero(entradaY, cy)

    if x < 0: x = 0
    if y < 0: y = 0
    if x > anchoCanvas: x = anchoCanvas
    if y > altoCanvas: y = altoCanvas

    if figuraActual == "circulo":
        lienzo.create_oval(x - radio, y - radio, x + radio, y + radio, fill=colorActual, outline=colorActual)
    elif figuraActual == "cuadrado":
        lienzo.create_rectangle(x - radio, y - radio, x + radio, y + radio, fill=colorActual, outline=colorActual)
    elif figuraActual == "triangulo":
        p1 = (x, y - radio )
        p2 = (x - radio, y + radio)
        p3 = (x + radio, y + radio)
        lienzo.create_polygon(p1, p2, p3, fill=colorActual, outline=colorActual)
        lienzo
def limpiar():
    lienzo.delete("all")

def saludar():
    nombre = entradaNombre.get().strip()
    if nombre == "":
        messagebox.showinfo("Saludo", "Escribe tu nombre 🙂")
        return
    texto = "¡Hola, {}!".format(nombre)
    etiquetaSaludo.config(text=texto)

def salir():
    ventana.destroy()


ventana = tk.Tk()
ventana.title("Práctica Tkinter CamelCase")
ventana.resizable(False, False)

panel = tk.Frame(ventana, padx=8, pady=8)
panel.grid(row=0, column=0, sticky="ns")

lienzo = tk.Canvas(ventana, width=anchoCanvas, height=altoCanvas, bg="white")
lienzo.grid(row=0, column=1, padx=8, pady=8)

etiquetaEstado = tk.Label(panel, text="Figura: Circulo | Color: black")
etiquetaEstado.grid(row=0, column=0, columnspan=3, pady=(0,8))

tk.Label(panel, text="Figuras", font=("Arial", 10, "bold")).grid(row=1, column=0, sticky="w", pady=(2,2))
btnCirculo = tk.Button(panel, text="Círculo", width=10, command=selCirculo)
btnCuadrado = tk.Button(panel, text="Cuadrado", width=10, command=selCuadrado)
btnTriangulo = tk.Button(panel, text= "triangulo", width=10, command=selTriangulo)
btnCirculo.grid(row=2, column=0, padx=2, pady=2)
btnCuadrado.grid(row=2, column=1, padx=2, pady=2)
btnTriangulo.grid(row=2, column=2, padx=2, pady=2)

tk.Label(panel, text="Colores", font=("Arial", 10, "bold")).grid(row=3, column=0, sticky="w", pady=(6,2))
btnNegro = tk.Button(panel, text="Negro", width=10, command=colNegro)
btnRojo = tk.Button(panel, text="Rojo", width=10, command=colRojo)
btnAzul = tk.Button(panel, text="Azul", width=10, command=colAzul)
btnVerde = tk.Button(panel, text="Verde", width=10, command=colVerde)
btnMorado = tk.Button(panel, text="morado", width=10, command=colMorado)
btnNegro.grid(row=4, column=0, padx=2, pady=2)
btnRojo.grid(row=4, column=1, padx=2, pady=2)
btnAzul.grid(row=4, column=2, padx=2, pady=2)
btnVerde.grid(row=5, column=0, padx=2, pady=2)
btnMorado.grid(row=5, column=1, padx=2, pady=2)

tk.Label(panel, text="Coordenadas (x, y)", font=("Arial", 10, "bold")).grid(row=6, column=0, sticky="w", pady=(6,2))
entradaX = tk.Entry(panel, width=10)
entradaY = tk.Entry(panel, width=10)
entradaX.grid(row=7, column=1, padx=2, pady=2, sticky="w")
entradaY.grid(row=8, column=1, padx=2, pady=2, sticky="w")
tk.Label(panel, text="x:").grid(row=7, column=0, sticky="e")
tk.Label(panel, text="y:").grid(row=8, column=0, sticky="e")

btnDibujar = tk.Button(panel, text="Dibujar", width=10, command=dibujar)
btnLimpiar = tk.Button(panel, text="Limpiar", width=10, command=limpiar)
btnDibujar.grid(row=9, column=0, padx=2, pady=(8,2))
btnLimpiar.grid(row=9, column=1, padx=2, pady=(8,2))

tk.Label(panel, text="Nombre", font=("Arial", 10, "bold")).grid(row=10, column=0, sticky="w", pady=(10,2))
entradaNombre = tk.Entry(panel, width=16)
entradaNombre.grid(row=11, column=0, columnspan=2, padx=2, pady=2, sticky="w")
btnSaludar = tk.Button(panel, text="Saludar", width=10, command=saludar)
btnSaludar.grid(row=11, column=2, padx=2, pady=2)
etiquetaSaludo = tk.Label(panel, text="", fg="blue")
etiquetaSaludo.grid(row=12, column=0, columnspan=3, pady=(2,8))

btnSalir = tk.Button(panel, text="Salir", width=10, command=salir)
btnSalir.grid(row=13, column=2, padx=2, pady=(6,2))

actualizarEstado()
ventana.mainloop()
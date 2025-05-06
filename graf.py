import tkinter
from pygame import mixer
from tkinter import ttk #Para la lista de cancionesssss
import pygame
from codigorepr import NodoCancion
from codigorepr import DbleEnlCircular

Listamusica = DbleEnlCircular()
ventana = tkinter.Tk()
ventana.geometry('1300x700')#Tamaño de la ventana
ventana.title("Myscy")
ventana.iconbitmap("simbolos/dvd.ico")

ventana.configure(bg="black")
contenedor1 = tkinter.Frame(ventana, bg="black")
contenedor1.pack(expand=True)  # expand True para centrar verticalmente
contenedor1.place(relx=0.1, rely=0.5, anchor="w") #relx porcentaje de largo y rely porcentaje de alto

etiquetaagreg = tkinter.Label(contenedor1, text="Añadir Cancion", fg="light cyan", bg="black", font=("Resist Mono", 25, "bold"))
etiquetaagreg.pack(pady="10")#espaciado
etiquetanombre = tkinter.Label(contenedor1, text="Nombre de la Cancion", fg="DarkSlateGray1", bg="black", font=("Arial", 15, "bold"))
etiquetanombre.pack(pady="2")
entradanombre = tkinter.Entry(contenedor1, fg="white", bg="gray5", font=("Arial", 15, "bold"))
entradanombre.pack(pady="10")

etiquetaartista = tkinter.Label(contenedor1, text="Nombre del Artista", fg="DarkSlateGray1", bg="black", font=("Arial", 15, "bold"))
etiquetaartista.pack(pady="2")
entradaartista = tkinter.Entry(contenedor1, fg="white", bg="gray5", font=("Arial", 15, "bold"))
entradaartista.pack(pady="10")

etiquetatiempo = tkinter.Label(contenedor1, text="Tiempo de la Cancion", fg="DarkSlateGray1", bg="black", font=("Arial", 15, "bold"))
etiquetatiempo.pack(pady="2")
entradatiempo = tkinter.Entry(contenedor1, fg="white", bg="gray5", font=("Arial", 15, "bold"))
entradatiempo.pack(pady="10")

etiqruta = tkinter.Label(contenedor1, text="Ruta del mp3", fg="DarkSlateGray1", bg="black", font=("Arial", 15, "bold"))
etiqruta.pack(pady="2")
entraruta = tkinter.Entry(contenedor1, fg="white", bg="gray3", font=("Arial", 15, "bold"), textvariable="Carpeta/Musica.mp3")
entraruta.insert(0, "Musica/cancion.mp3")
entraruta.pack(pady="10")

encabzdo = tkinter.Label(ventana, text="Mi Musica :)", fg ="Dark Sea Green1", bg="black", font=("Comfortaa", 22, "bold"))
encabzdo.place(relx=0.7, rely=0.28, anchor="e")


listac = ttk.Treeview(ventana, columns=("Titulo", "Artista", "Tiempo"), show="headings")
listac.column("0",width=225, anchor="center")
listac.heading("0", text="Titulo")
listac.column("1", width=225, anchor="center")
listac.heading("1", text="Artista")
listac.column("2", width=200, anchor="center")
listac.heading("2", text="Tiempo")
listac.place(relx=0.88, rely=0.5, anchor="e")

style = ttk.Style()
style.theme_use("default")

style.configure("Treeview",
                background="black",
                foreground="white",
                fieldbackground="black",
                rowheight=25)

style.map("Treeview",
          background=[("selected", "#444444")],
          foreground=[("selected", "white")])

style.configure("Treeview.Heading",
                background="black",
                foreground="plum1",
                font=('Arial', 12, 'bold'))

def Agregarcancion():
    global contador
    nombre = entradanombre.get()
    artista = entradaartista.get()
    tiempo = entradatiempo.get()
    ruta = entraruta.get()
    nuevasong = NodoCancion(nombre, artista, tiempo, ruta)
    Listamusica.Insertar(nuevasong)
    Listamusica.Listar()
    listac.insert("", "end", values=(nombre, artista, tiempo))

    
    
boton = tkinter.Button(contenedor1, text="Agregar Canción :o",fg="DarkSeaGreen1", bg="gray3", font=("Arial", 15, "bold"), command=Agregarcancion)
boton.pack(anchor="center")

contenedorreproducir = tkinter.Frame(ventana, bg="black")
contenedorreproducir.pack(expand=True)
contenedorreproducir.place(relx=0.5, rely=0.8, anchor="n")

CancionAhora = None
Sinoreproduce = False
Cancion = None
EstaPausada = False
cual = 1



def ReproducirPausar():
    global CancionAhora, Sinoreproduce, Cancion, Listamusica, EstaPausada, cual, botplaystop, iconopausarepr
    pygame.init()
    mixer.init()  

    if EstaPausada:
        mixer.unpause()
        EstaPausada = False
        iconopausarepr()
        return

    if mixer.get_busy():
        mixer.pause()
        EstaPausada = True
        iconopausarepr()
        return

    if not Sinoreproduce:
        CancionAhora = Listamusica.Cabeza
        iconopausarepr()
        Sonar()

def iconopausarepr():
    global cual, botplaystop
    if cual == 1:
        botplaystop = tkinter.PhotoImage(file="simbolos/playm.png")
        cual = 2
    else:
        botplaystop = tkinter.PhotoImage(file="simbolos/stopm.png") 
        cual = 1
    botonreproductor = tkinter.Button(contenedorreproducir, image=botplaystop,bg = "black", borderwidth=0,activebackground="black", compound="top", command=ReproducirPausar)
    botonreproductor.grid(row=0, column=1, padx=10)

iconopausarepr()

texto_dinamico = tkinter.StringVar()
texto_dinamico.set("Ingrese Cancion")
cualsuena = tkinter.Label(ventana, textvariable=texto_dinamico, bg="black", fg="goldenrod1")
cualsuena.place(relx=0.5, rely=0.9, anchor="n")
def Sonar():
    global CancionAhora, Sinoreproduce, Cancion, EstaPausada
    pygame.init()
    mixer.init()
    try:
        rutacan = CancionAhora.Valor.Rutaarchivo
        Cancion = mixer.Sound(rutacan)
        Cancion.play()
        EstaPausada = False
        Sinoreproduce = True
        Suenaono()
        texto_dinamico.set(f"{CancionAhora.Valor.Nombrecancion} - {CancionAhora.Valor.Artista}")
    except Exception as e:
        print("Error al reproducir:", e)

def Suenaono():
    global CancionAhora, Sinoreproduce, EstaPausada

    if mixer.get_busy() or EstaPausada:
        ventana.after(500, Suenaono)
    else: 
        CancionAhora = CancionAhora.Siguiente
        Sonar()

def cancionsiguiente():
    global CancionAhora
    mixer.quit()
    CancionAhora = CancionAhora.Siguiente
    Sonar()

def cancionanterior():
    global CancionAhora
    mixer.quit()
    CancionAhora = CancionAhora.Anterior
    Sonar()



simbanterior = tkinter.PhotoImage(file="simbolos/hacia-atras.png")
botonreproductor = tkinter.Button(contenedorreproducir, image=simbanterior, bg = "black", borderwidth=0, activebackground="black", compound="top", command=cancionanterior)
botonreproductor.grid(row=0, column=0, padx=10)

simbsiguiente = tkinter.PhotoImage(file="simbolos/siguiente-boton.png")
botonreproductor = tkinter.Button(contenedorreproducir, image=simbsiguiente, bg = "black", borderwidth=0,activebackground="black", compound="top", command=cancionsiguiente)
botonreproductor.grid(row=0, column=2)


ventana.mainloop()
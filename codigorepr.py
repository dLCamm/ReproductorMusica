import pygame
from pygame import mixer

class NodoCancion:
    def __init__(self, nombre, artista, duracion, ruta):
        self.Nombrecancion = nombre
        self.Artista = artista
        self.Duracion = duracion
        self.Rutaarchivo = ruta

    def Imprimir(self):
        print(self.Nombrecancion, self.Artista, self.Duracion, self.Rutaarchivo)


class Nodo:
    def __init__(self, valor):
        self.Siguiente = None
        self.Anterior = None
        self.Valor = valor
    

class DbleEnlCircular:
    def __init__(self):
        self.Cabeza = None

    def Insertar(self, dto):
        Dato = Nodo(dto)
        if not self.Cabeza:
            self.Cabeza = Dato
            self.Cabeza.Siguiente = self.Cabeza
            self.Cabeza.Anterior = self.Cabeza

        else:
            newDato = self.Cabeza.Anterior
            Dato.Siguiente = self.Cabeza
            Dato.Anterior = newDato
            newDato.Siguiente = Dato
            self.Cabeza.Anterior = Dato
        
    def Eliminar(self, nombrecancion):
        if self.Cabeza == None:
            return "No existen Canciones"
        ahora = self.Cabeza
        if ahora.Valor.Nombrecancion == nombrecancion:
            if ahora.Siguiente == None:
                ahora = None
            else:
                ahora.Anterior.Siguiente = ahora.Siguiente
                ahora.Siguiente.Anterior = ahora.Anterior
                self.Cabeza = ahora.Siguiente
        else:
            ahora = self.Cabeza.Siguiente
            while ahora != self.Cabeza:
                if ahora.Valor.Nombrecancion == nombrecancion:
                    ahora.Anterior.Siguiente = ahora.Siguiente
                    ahora.Siguiente.Anterior = ahora.Anterior
    
    def Listar(self):
        print("¿Lista Canciones?")
        
        ahora = self.Cabeza.Siguiente
        if ahora == None:
            print("No hay datos")
        else:
            self.Cabeza.Valor.Imprimir()
            while ahora != self.Cabeza:
                ahora.Valor.Imprimir()
                ahora = ahora.Siguiente
                   





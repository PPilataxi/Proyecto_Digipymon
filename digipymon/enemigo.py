"""
Esta clase  tiene los atributos del jugador:
nombre,lista digipymon como un diccionario vacio ,cantidad digipymon inicializado a 0
sirve para que el enemigo pueda enfrentarse con el jugador    
"""
class Enemigo():
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    """
    Este metodo sirve para añadir  un digipymon a la lista de digipymons 
    Se añade a la lista con un append y la variable digipymon 
    y se suma 1 en la cantidad de digipymon 
    """
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
    
from digipymon import Digipymon;

class Enemigo():
    def __init__( self,nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self,digipymon):

        poyomon =  Digipymon("pollo",12,13,"fuego",2)  
        self.lista_digipymon.append(poyomon) 
        self.cantidad_digipymon += 1 

    def __str__(self):
        return f"Nombre: {self.nombre}, lista_digipymon:{self.lista_digipymon},cantidad_digipymon:{self.cantidad_digipymon}"

        
enemego = Enemigo(nombre="patata")
poyomon =  Digipymon("pollo",12,13,"fuego",2)  

enemego.añadir_digipymon(poyomon)
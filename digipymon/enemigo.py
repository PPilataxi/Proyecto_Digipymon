from digipymon import  Digipymon;

class Enemigo():
    def __init__( self,nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self):

        poyomon =  Digipymon("pollo",12,13,"fuego",2)  
        self.lista_digipymon[poyomon] 
        self.cantidad_digipymon + 1 
        print(self.lista_digipymon)

        print(poyomon.ataque)

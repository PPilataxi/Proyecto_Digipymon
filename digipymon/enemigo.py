from digipymon import  Digipymon;

class Enemigo():
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

    def añadir_digipymon(self,digipymon):

        poyomon =  Digipymon("pollo",12,13,"fuego",2)  
        self.lista_digipymon.append(poyomon) 
        self.cantidad_digipymon += 1 
       
        #for iterador in  self.lista_digipymon:
            #print(iterador)
        def __repr__(lista_digipymon):
            return print(str(self.lista_digipymon.__dict__))

        
enemego = Enemigo(nombre="patata")

poyomon =  Digipymon("pollo",12,13,"fuego",2)
enemego.añadir_digipymon(poyomon)
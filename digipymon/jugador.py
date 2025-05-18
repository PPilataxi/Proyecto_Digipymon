"""
Esta clase  tiene los atributos del jugador:
  nombre,lista digipymon como un diccionario vacio ,cantidad digipymon inicializado a 0, las monedas del juego digicoins inicializado a 0
sirve para que el jugador pueda interactuar con el programa    
"""
class Jugador():
    def __init__(self, nombre):

            self.nombre = nombre
            self.lista_digipymon = []
            self.cantidad_digipymon = 0
            self.digicoins = 10
    
    """
    Este metodo sirve para añadir  un digipymon a la lista de digipymons 
    Se añade a la lista con un append y la variable digipymon 
    y se suma 1 en la cantidad de digipymon 
    """
    def añadir_digipymon(self, digipymon):
            self.lista_digipymon.append(digipymon)
            self.cantidad_digipymon += 1
            

    """
    Este metodo sirve para consultar los digipymons  que tiene el jugador  
    para ello comprueba si el digipymon esta en la lista de digipymons 
    Si esta , los imprime 
    y sino esta devuelve un print de que no esta en la lista  
    """
    def consultar_digipymon(self):
            if self.lista_digipymon:
                for digipymon in self.lista_digipymon:
                    print (f"Estos son tus digipymon: {digipymon}" )
                    
            else:
                print(f"{self.nombre} aún no tiene ningún digipymon en su colección")



    """
    Este metodo sirve para consultar las digicoins que tiene el jugador  
    para ello devuelve un print con el nombre del jugador y las digicoins que este tiene 

    """
    def consultar_digicoins(self):
            print(f"{self.nombre} tiene en su posesión {self.digicoins} digicoins")

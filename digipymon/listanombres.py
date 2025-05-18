
import random
"""
Esta clase sirve para que los digipymon y los entrenadores tengan nombres aleatorios cada vez que generamos uno 
para ello tiene como atributos  dos listas una con 20 nombres de digipymons 
y otra con 20 nombres de entrenadores 
para hacerlo aleatorio se importa la clase ramdon y se usa ramdom randint de 0a 20 , aunque tambien se podria haber usado random.choice 

"""
class ListaNombres():
        def __init__( self ):
                self.lista_nombres_digipymons = ["digimon","poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"]
                self.lista_nombres_entrenadores = ["patata","carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"]

        """
        Este metodo sirve para darle al digipymon un nombre aleatorio cada vez 
        para ello usamos la variable numeroaleatorio para guardar un nombre al azar de digipymon 
        devuelve numeroaleatorio 
        """
        def obtener_nombre_digipymon(self):

                numeroaleatorio = self.lista_nombres_digipymons[random.randint(0, 20)] 
                return numeroaleatorio
                
        """
        Este metodo sirve para darle al entrenador un nombre aleatorio cada vez 
        para ello usamos la variable entrenadoraleatorio para guardar un nombre al azar de digipymon
        devuelve  entrenadoraleatorio
        """
        def obtener_nombre_entrenador(self):
                entrenadoraleatorio = self.lista_nombres_entrenadores[random.randint(0, 20)] 
                return entrenadoraleatorio
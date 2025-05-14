
import random
class ListaNombres():
    def __init__( self ):
       self.lista_nombres_digipymons = ["digimon","poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"]
       self.lista_nombres_entrenadores = ["patata","carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"]


    def obtener_nombre_digipymon(self):

            numeroaleatorio = self.lista_nombres_digipymons[random.randint(0, 20)] 
            return numeroaleatorio
         

    def obtener_nombre_entrenador(self):
               entrenadoraleatorio = self.lista_nombres_entrenadores[random.randint(0, 20)] 
               return entrenadoraleatorio
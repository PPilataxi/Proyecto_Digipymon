
import random
class ListaNombres():
    def __init__( self ,lista_nombres_digipymons,lista_nombres_entrenadores ):
       self.lista_nombres_digipymons = ["digimon","poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"]
       self.lista_nombres_entrenadores = ["patata","carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"]


    def obtener_nombre_digipymon(self,lista_nombres_digipymons):

            numeroaleatorio = self.lista_nombres_digipymons[random.randint(0, 20)] 
            return print(numeroaleatorio)
         

    def obtener_nombre_entrenador(self):
               entrenadoraleatorio = self.lista_nombres_entrenadores[random.randint(0, 20)] 
               return print(entrenadoraleatorio)
    

def main():
       nombre = ListaNombres()
       ListaNombres.obtener_nombre_digipymon


main()
print(ListaNombres.obtener_nombre_entrenador)
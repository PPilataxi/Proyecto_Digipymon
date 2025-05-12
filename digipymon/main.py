#from inventario import Inventario; 

#from digipymon import Digipymon;

#from enemigo import Enemigo;
from listanombres import ListaNombres

#bolsa = Inventario(objetos = {"patata" : 1,"naranja": 2})
#bolsa.usar_objeto()
#print(bolsa.objetos)

#enemego = Enemigo.__init__(nombre="manuel")
#enemego.añadir_digipymon()

#lista_nombres_entrenadores=["carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"] 

#lista = ListaNombres.__init__(self,lista_nombres_digipymons=["poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"],lista_nombres_entrenadores = ["carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"] )

lista = ListaNombres(lista_nombres_digipymons=["digimon","poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"],lista_nombres_entrenadores=["carlos","pepe","loli" ,"naruto","sasuke","jack","elias","hector","daniel","nerea","claudia","pablo","raul","kiko","raquel","susana","jose","sakura","nosferatu","juan"] )    
lista.obtener_nombre_digipymon(lista_nombres_digipymons=["digimon","poyomon","pilamon","eliomon","poliomon","jijomon","dodomon","cinomon","sakomon","suliamon","kikamon","poyimon","polomon","eluomon","piliomon","jojomon","dadomon","cunomon","sekomon","saliamon","kakumon"])
lista.obtener_nombre_entrenador() 
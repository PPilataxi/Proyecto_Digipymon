from inventario import Inventario; 

from digipymon import Digipymon;

from enemigo import Enemigo;

bolsa = Inventario(objetos = {"patata" : 1,"naranja": 2})
bolsa.usar_objeto()
print(bolsa.objetos)

enemego = Enemigo()
enemego.añadir_digipymon()
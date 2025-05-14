from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random

def generar_digipymon_aleatorio():
        lista_digipymon = ListaNombres() 
        
        nombre = lista_digipymon.lista_nombres_digipymons
        lista_tipo = ["fuego","agua","planta"]    

        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        nivel = random.randint(1, 3)
        tipo = random.choice(lista_tipo)

        doyi = Digipymon(nombre,vida,ataque,nivel,tipo)

        return doyi.__str__()           
    
    

def menu():
        print("*****¿Qué desea hacer?*****")
        print("1. Buscar digipymon")
        print("2. Luchar contra un entrenador")
        print("3. Ir a la tienda")
        print("4. Usar OBjetos")
        print("5. Consultar inventario")
        print("6. Consultar digipymon")
        print("7. Buscar digipymon")

        return menu
        


def buscar_digipymon():
        pass

def combate():
        pass

def digishop(jugador, inventario):
        print("*****Bienvenido a la digishop*****")
        print("*****¿Qué desea comprar?*****")
        print("a. Digipyballs: 5 digicoins")
        print("b. Energetica: 3 digicoins (+ 10p digisalud)")
        print("c. Trembolóna: 4 digicoins (+5p de aura )")
        

def usar_item(yuyu):
        bolsa = Inventario(objetos= {})
        bolsa.añadir_objeto(nombre="uva",cantidad=4)
        print(bolsa.objetos)
        print("Que item deseas usar ?")
        if input == 1:
         print("Quieres usar  energetica")
        print("¿En que digipymon deseas usarlo?")
        
        if input == 2:
            print("Quieres usarlo en  doyi") 
            #energetica = doyi.__getattribute__vida + 10   
            #doyi.__setattr__vida =energetica
        else:
            
            input == 2
            print("Quieres usar  trembolona")
            print("¿En que digipymon deseas usarlo?")
        
        if input == 1:
            print("Quieres usarlo en  doyi") 
            #tembolona = doyi.__getattribute__ataque + 10   
            #doyi.__setattr__ataque =tembolona
                
        

def main():
       yuyu= generar_digipymon_aleatorio()
       #usar_item()

main()
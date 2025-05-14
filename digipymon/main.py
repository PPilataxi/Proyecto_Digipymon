from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random

def generar_digipymon_aleatorio():
        lista_digipymon = ListaNombres() 
        
        nombre = lista_digipymon.obtener_nombre_digipymon()
        lista_tipo = ["fuego","agua","planta"]    

        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        nivel = random.randint(1, 3)
        tipo = random.choice(lista_tipo)

        doyi = Digipymon(nombre,vida,ataque,tipo,nivel)

        return doyi       
    
    

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

def digishop():
        jugador1 = Jugador("tifon")
        bolsa = Inventario()
        
        print("*****Bienvenido a la digishop*****")
        print("*****¿Qué desea comprar?*****")
        print("a. Digipyballs: 5 digicoins")
        print("b. Energetica: 3 digicoins (+ 10p digisalud)")
        print("c. Trembolóna: 4 digicoins (+5p de aura )")
        salir_tienda = True
        while salir_tienda == True:
         jugador1.consultar_digicoins()
         opcion = input() 
         if opcion == "a" :
               if jugador1.digicoins < 5:
                    print("no tienes fondos")
                    salir_tienda == False
               else:      
                bolsa.añadir_objeto("Digipyballs",1)
                print(bolsa.objetos)
                compra1 =jugador1.digicoins - 5
                jugador1.digicoins = compra1
                jugador1.consultar_digicoins()
                salir_tienda == False
                menu()
         elif opcion == "b" :
                if jugador1.digicoins < 3:
                    print("no tienes fondos")
                    salir_tienda == False
                else:    
                 bolsa.añadir_objeto("energetica",1)
                 print(bolsa.objetos)
                 compra2 =jugador1.digicoins - 3
                 jugador1.digicoins = compra2
                 jugador1.consultar_digicoins()
                 salir_tienda == False
         elif opcion == "c" :
                if jugador1.digicoins < 4:
                    print("no tienes fondos")
                    salir_tienda == False
                else:    
                 bolsa.añadir_objeto("Trembolona",1)
                 print(bolsa.objetos)
                 compra3 =jugador1.digicoins - 4
                 jugador1.digicoins = compra3
                 jugador1.consultar_digicoins()
                 salir_tienda == False   

def usar_item(yuyu,bolsa):
        

       
        print(bolsa.objetos)
        print("Que item deseas usar ?")
        num2 = int(input("Pulsa 1 para usar energetica " \
                         "2 para usar trembolona"))
        
        print("has pulsado   " + str(num2))   
        if num2 == 1:
         print("Quieres usar  energetica")
        print("¿En que digipymon deseas usarlo?")
        num1 = int(input("Pulsa 1 para usarlo en yuyu " \
                         "2 para usarlo en yaya"))
        if num1 == 1:
            print("Quieres usarlo en  yuyu") 
            energetica = yuyu.vida + 10   
            yuyu.vida = energetica
            print( " vida: " + str(yuyu.vida)  )
        elif num2 == 2:

            print("Quieres usar  trembolona")
            print("¿En que digipymon deseas usarlo?")
        num1 = int(input("Pulsa 1 para usarlo en yuyu " \
                         "2 para usarlo en yaya"))
        if num1 == 1:
            print("Quieres usarlo en  yuyu") 
            tembolona = yuyu.ataque + 5   
            yuyu.ataque =tembolona
            print(  " ataque: "+ str(yuyu.ataque) )    
        

def main():
       yuyu= generar_digipymon_aleatorio()
       #print(" nombre: " + yuyu.nombre , " vida: " + str(yuyu.vida) , " ataque: "+ str(yuyu.ataque) , " tipo: "+ yuyu.tipo , " nivel: "+ str(yuyu.nivel))
       
       menu()
       eleccion =input()
       if eleccion == str(3):
         digishop()
       elif eleccion == str(4): 
         usar_item(yuyu, bolsa = Inventario())
         print( " vida: " + str(yuyu.vida) , " ataque: "+ str(yuyu.ataque) )
main() 
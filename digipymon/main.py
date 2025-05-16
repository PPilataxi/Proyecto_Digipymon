from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random
jugador1 = Jugador("tifon")


bolsa = Inventario()       



def menu():

    print("*****¿Qué desea hacer?*****")
    print("1. Buscar digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar Objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymons")
    print("7. Salir")
    
    eleccion =int(input())
    return eleccion       
    
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
    






def buscar_digipymon():
        pass

def combate():
        pass

def digishop( ):
        
    salir_tienda = True
    while salir_tienda: 
        print("*****Bienvenido a la digishop*****")
        print("*****¿Qué desea comprar?*****")
        print("a. Digipyballs: 5 digicoins")
        print("b. Energetica: 3 digicoins (+ 10p digisalud)")
        print("c. Trembolóna: 4 digicoins (+5p de aura )")
        jugador1.consultar_digicoins()
        
        
        opcion = input() 
        if opcion == "a" :
            if jugador1.digicoins < 5:
                print("no tienes fondos")
                
                

            else:      
             bolsa.añadir_objeto("Digipyballs",1)
             print(bolsa.objetos)
            
             compra1 =jugador1.digicoins - 5
             jugador1.digicoins = compra1
             jugador1.consultar_digicoins()
             print("se ha añadido al inventario")
             print("que quieres hacer ahora ")
             tienda = int(int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) )
             if tienda == 2 :
                print("estas saliendo de la tienda ")
                salir_tienda = False 
                                    

             elif jugador1.digicoins == 0:
                
                print("no tienes fondos")
                
                
        
            
        elif opcion == "b" :
            if jugador1.digicoins < 3:
                print("no tienes fondos")
                salir_tienda = False
                
            else:    
                bolsa.añadir_objeto("energetica",1)
                print(bolsa.objetos)
                
                compra2 =jugador1.digicoins - 3
                jugador1.digicoins = compra2
                jugador1.consultar_digicoins()
                print("se ha añadido al inventario")
                print("que quieres hacer ahora ")
                tienda = int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) 
                if tienda == 1 :
                 digishop()
                elif tienda == 2 :
                    print("estas saliendo de la tienda ")
                    salir_tienda = False 
                    

                elif jugador1.digicoins == 0:
                
                    print("no tienes fondos")
                
                    salir_tienda = False
        elif opcion == "c" :
            if jugador1.digicoins < 4:
                print("no tienes fondos")
                salir_tienda = False
                
            else:    
                bolsa.añadir_objeto("Trembolona",1)
                print(bolsa.objetos)
                
                compra3 =jugador1.digicoins - 4
                jugador1.digicoins = compra3
                jugador1.consultar_digicoins()
                print("se ha añadido al inventario")
                print("que quieres hacer ahora ")
                tienda = int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) 
                if  tienda == 2 :
                    print("estas saliendo de la tienda ")
                    salir_tienda = False 
                        

                elif jugador1.digicoins == 0:
                    
                    print("no tienes fondos")
                
                
        elif opcion == "d" :
                    
            salir_tienda = False 


def usar_item(yuyu):
        

        
        print(bolsa.objetos )
        print("Que item deseas usar ?")
        num2 = int(input("Pulsa 1 para usar energetica " \
                         "2 para usar trembolona  "\
                         "3 para intentar darle una  digiball al digipymon  " ))
        
         
        if num2 == 1:
         
          print("Quieres usar  energetica")
          print("¿En que digipymon deseas usarlo?")
          num1 = int(input("Pulsa 1 para usarlo en yuyu " \
                         "2 para usarlo en yaya " ))
        
         
          if num1 == 1:
            print("Quieres usarlo en  yuyu") 
            energetica = yuyu.vida + 10   
            yuyu.vida = energetica
            print( "la vida de yuyu ahora es : " + str(yuyu.vida)  )
            bolsa.usar_objeto("energetica")
            print(bolsa.objetos)
            menu()
        elif num2 == 2:

            print("Quieres usar  trembolona")
            print("¿En que digipymon deseas usarlo?")
            num1 = int(input("Pulsa 1 para usarlo en yuyu " \
                         "2 para usarlo en yaya " ))
            if num1 == 1:
             print("Quieres usarlo en  yuyu") 
             tembolona = yuyu.ataque + 5   
             yuyu.ataque =tembolona
             print(  " el ataque de yuyu ahora "+ str(yuyu.ataque) )    
             bolsa.usar_objeto("trembolona")
             print(bolsa.objetos)
             menu()
        elif num2 == 3:

            print("Quieres  intentar darle una  digiball al digipymon  ")
            print("el digipymon se queda mirando la digiball  , tras 5 minutos la cojes para que pueda centrarse en el combate ")
            usar_item(yuyu)

def Consultar_inventario(bolsa):
    print(bolsa.objetos)
    menu()

def Consultar_digipymons():
    jugador1.añadir_digipymon()
    print(jugador1.lista_digipymon)
    menu()

def main():
    
    yuyu= generar_digipymon_aleatorio()
      
    print("Un dia  decidiste conquistar el mundo de los digipymon para ello,  ")
    print("te embarcaste en una gran aventura  ")
    bolsa.añadir_objeto("energetica",1)
    bolsa.añadir_objeto("Digipyballs",3)
    print("empiezas con una energetica y 3 digiballs")
    nombre_jugador = input("Dinos tu nombre ")
    jugador1.nombre = nombre_jugador
    #print(jugador1)
    print("este es tu digipymon inicial ")
    print(" nombre: " + yuyu.nombre , " vida: " + str(yuyu.vida) , " ataque: "+ str(yuyu.ataque) , " tipo: "+ yuyu.tipo , " nivel: "+ str(yuyu.nivel))
    salir =True
    while salir:   
        opcion = menu()
        

        if opcion == 3:
            digishop()
        elif opcion == 4: 
            usar_item(yuyu)
        elif opcion == 5: 
            Consultar_inventario(bolsa.objetos) 
        elif opcion == 6: 
            Consultar_digipymons()
        elif opcion == 7: 
            print("saliendo del programa")
            salir = False
            

      
main() 
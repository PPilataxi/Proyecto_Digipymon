from digipymon import digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random

def generar_digipymon_aleatorio():
    pass


def menu():
    print("*****¿Qué desea hacer?*****")
    print("1. Buscar digipymon")
    print("2. Luchar contra un entrenador")
    print("3. Ir a la tienda")
    print("4. Usar Objetos")
    print("5. Consultar inventario")
    print("6. Consultar digipymon")
    print("7. Buscar digipymon")

    opcion = int(input("Elige una opción: "))
    if 1 <= opcion <= 7:
        return opcion
    else:
        print("ERROR, no existe esa opción. Ingrese una opción correcta")
    return menu
    


def buscar_digipymon(self, jugador, inventario):
#Introducción a la función
    print("******Es la hora de buscar digipymons******")
    digipymon_salvaje = self.generar_digipymon_aleatorio(lista_nombres)
    print(f"¡OMFG, {digipymon_salvaje} apareció para torturarte!")

#Probabilidad de capturar el digipyball
    probabilidad_captura = max(0, 100 - (digipymon_salvaje.nivel * 10))
    print(f"Probabilidad de captura: {probabilidad_captura}%")

#Decisión de captura
    while True:
        decision = input("¿Quiéres intentar atraparlo con tus digibolas ;) (si/no)?").lower()

        if decision == si:
            jugador.cantidad_digipymons
        elif decision == no:

        else:
            
            break


def combate():
    pass

def digishop(jugador, inventario):
    print("*****Bienvenido a la digishop*****")
    print("*****¿Qué desea comprar?*****")
    print("a. Digipyballs: 5 digicoins")
    print("b. Energetica: 3 digicoins (+ 10p digisalud)")
    print("c. Trembolóna: 4 digicoins (+5p de aura )")
    jugador1 = jugador()
    salir_tienda = True
    while salir_tienda == True:
        jugador1.consultar_digicoins()
        opcion = input() 
        if opcion == "a" :
            if jugador1.digicoins < 5:
                print("no tienes fondos")

        
        
        

    # Si tiene dinero: se añade al inventario el objeto y se resta el dinero del bolsillo
    # Si no tiene dinero: le dices que esta pobre y se va de la tienda
    
    

def usar_item():
    pass

def main():
    pass
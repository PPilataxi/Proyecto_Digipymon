from digipymon import digipymon
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
    print(f"Tienes un {probabilidad_captura}% de posibilidades de llevarte este digipymon")

#Decisión de captura
    while True:
        decision = input("¿Quiéres intentar atraparlo con tus digibolas ;) (si/no)?").lower()

        if decision == si:
            if "Digipyball" in inventario.objetos and inventario.objetos


def combate():
    pass

def digishop(jugador, inventario):
        print("*****Bienvenido a la digishop*****")
        print("*****¿Qué desea comprar?*****")
        print("a. Digipyballs: 5 digicoins")
        print("b. Energetica: 3 digicoins (+ 10p digisalud)")
        print("c. Trembolóna: 4 digicoins (+5p de aura )")
        print("d. Volver al menú")
        
        while True:
            opcion = int(input("Elija un objeto que desea comprar: ").lower())
            #Condición if 
            if opcion == a:
                if jugador.consultar_digicoins >= 5:
                    inventario.añadir_objeto("Digipyball", 1)
                    jugador.consultar_digicoins -=5
                    print("Has apostado a las digipyballs")
                else:
                    print("Andas pobre, ponte a chambear")
            elif opcion == b:
                if jugador.consultar_digicoins >= 3:
                    inventario.añadir_objeto("Energetica", 1)
                    jugador.consultar_digicoins -=3
                    print("Has decidido poner a tu digipymon con el corazón al fallo comprando la ENERGETICA")
                else:
                    print("Andas pobre, apuesta todo lo que tienes al rojo")
            elif opcion == c:
                if jugador.consultar_digicoins >= 4:
                    inventario.añadir_objeto("Trembolona", 4)
                    jugador.consultar_digicoins -=4
                    print("Tu digipymon se pondrá mamadisimo con la TREMBOLONA")
                else:
                    print("Andas pobre, culpa de Pedro Sanchez, DIMISIÓN")
            elif opcion == d:
                break
            else:
                print("Opción valida")
            print(f"Te quedan: {jugador.consultar_digicoins}")















def usar_item():
    pass

def main():
    pass
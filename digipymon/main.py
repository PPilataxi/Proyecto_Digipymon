from digipymon import digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random
def __init__(self):
    pass


def generar_digipymon_aleatorio(self, lista_nombres):
        lista_digipymon = ListaNombres() 
        
        nombre = lista_digipymon.obtener_nombre_digipymon()
        vida = random.randint(10, 20)
        ataque = random.randint(1, 10)
        nivel = random.randint(1, 3)
        lista_tipo = ["fuego","agua","planta"] 
        tipo = random.choice(lista_tipo)
        doyi = (nombre,vida,ataque,tipo,nivel)
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
    


def buscar_digipymon(self, jugador, inventario, lista_nombres):
#Introducción a la función
    print("******Es la hora de buscar digipymons******")
    el_rebelde = self.generar_digipymon_aleatorio(lista_nombres)
    print(f"¡OMFG, {el_rebelde} apareció para torturarte!")

#Probabilidad de capturar el digipyball
    captura_porcentaje= max(0, 100 - (el_rebelde.nivel * 10))
    print(f"Tienes un {captura_porcentaje}% de posibilidades de llevarte este digipymon")

#Decisión de captura
    while True:
        si_no = input("¿Quiéres intentar atraparlo con tus digibolas ;) (si/no)?").lower()
        if si_no == "si":
            if "Digipyball" in inventario.objetos and inventario.objetos["Digipyballs"] > 0:
                if jugador.cantidad_digipymon < 6:
                    inventario.usar_objeto("Digipyball")
                    if random.randint(1,100) <= captura_porcentaje:
                        print(f"Lograste capturar a este digipymon {el_rebelde.nombre}, Felicidades, era muy dificil")
                        jugador.añadir_digipymon(el_rebelde)
                        break
                    else:
                        print(f"¡¿Como se te puede haber escapado {el_rebelde.nombre}?! Afina la punteria Broh...")
                        break
                else:
                    print("Tienes todo tu ejercito completo")
                    break
            else:
                print("¿No te has dado cuenta de que no tienes Digyballs? COMPRA YA CARAJO!!!")
                break
        elif si_no == no:
            print("Le tuviste miedo al exito e hiciste bomba de humo frente al digipymon")
            break
        else:
            print("O no sabes leer, o no sabes escribir, ponga si o no por favor.")


def combate(self, jugador, lista_nombres):
    if not jugador.lista_digipymon:
        print("No dispones de ejercito para luchar por la República")
        return
    
    nombre_rival = lista_nombres.obtener_nombre_entrenadores()
    rival = Enemigo(nombre_rival)
    print(f"OMG, apareció {rival.nombre} y se quiere hacer un 1pa1 contra tí.")

    for x in range(jugador.cantidad_digipymon):
        rival.añadir_digipymon(self.generar_digipymon_aleatorio(lista_nombres))

    print(f"{rival.nombre} tiene reclutado a los siguientes Digipymons")
    for i, digipymon in enumerate(rival.lista_digipymon):
        print(f"{i + 1 }. {digipymon.nombre} (Vida: {digipymon.vida}, Ataque: {digipymon.ataque})")

    while True:
        pelea = input("¿Desea enfrentarse en el 1 vs 1 ? (si/no)").lower()
        if pelea == "si":
            victoria =0
            derrota = 0
            empate = 0

            print("*-*-*-*-* HORA DEL COMBATE *-*-*-*-*")
            for i in range(min(len(jugador.lista_digipymon, ), len(rival.lista_digipymon))):
                mi_soldado = jugador.lista_digipymon[i]
                soldado_rival = rival.lista_digipymon[i]
                print(f" ----- COMBATE -----")
                print(f"Va combatir {mi_soldado.nombre} (Vida: {mi_soldado.vida}, Ataque: {mi_soldado.ataque}) ***** VS ***** {soldado_rival.nombre} (Vida: {soldado_rival.vida} Ataque: {soldado_rival.ataque})")

                if mi_soldado.vida <= 0:
                    print(f"OHHH {mi_soldado.nombre} se ha quedado sin vida! LO FUSILARON! (Vida:{mi_soldado.vida})")
                    derrota +=1




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















def usar_item(self, jugador, inventario):
print(bolsa.objetos )
        print("Que item deseas usar ?")
        num2 = int(input("Pulsa 1 para usar energetica " \
                         "2 para usar trembolona " ))
        
        print("has pulsado   " + str(num2))   
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
            bolsa.usar_objeto()
            print(bolsa.objetos)





pass


def main():
    pass
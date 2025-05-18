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
                    continue

                if mi_soldado.ataque > soldado_rival.ataque:
                    print(f"")




def digishop(jugador, inventario):

    salir_tienda = True
    while salir_tienda:

        print("*****Bienvenido a la digishop*****")
        print("*****¿Qué desea comprar?*****")
        print("a. Digipyballs: -----> 5 digicoins")
        print("b. Energetica: -----> 3 digicoins (+ 10p digisalud)")
        print("c. Trembolóna: -----> 4 digicoins (+5p de aura )")
        print("d. Volver al menú")
        jugador.consultar_digicoins
        
        opcion = int(input("Elija un objeto que desea comprar: ").lower())
            if opcion == a:
                if  
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
    salir_items = True
    while salir_items:
        
    
        print(f"Que item quieres usar?\n {self.bolsa.objetos} \n 1. Digipyball\n 2. energica\n 3. Anabolizantes\n 4. Salir")
        respuesta_items = int(input("Escribe el número  "))
        if respuesta_items == 1 :
                
            print("Quieres  intentar darle una  digiball al digipymon  ")
            print("el digipymon se queda mirando la digiball  , tras 5 minutos la cojes para que pueda centrarse en el combate ")
        elif respuesta_items == 4 :
            salir_items = False
        elif respuesta_items == 2 :
            if "energetica"in self.bolsa.objetos:
                    
                    respuesta_digi = int(input(f"Sobre que digipymon quieres usar la energica {self.jugador1.consultar_digipymon()}?\n (escribe el Id o 'salir') "))
                    for digipymon in self.jugador1.lista_digipymon:
                        try:
                            if  self.digipymon.id == respuesta_digi:                        
                                self.digipymon.vida += 10
                                print(f"Le das la energetica a {self.digipymon.nombre} ") 
                                        
                                print("Glup!!")
                                        
                                print(f"{self.digipymon.nombre} ahora tiene {self.digipymon.vida} puntos de vida.")
                                input("Pulsa Enter para continuar...")
                                self.bolsa.usar_objeto("energetica") 
                                break
                            elif respuesta_digi == "salir":
                                salir_items = False
                        except ValueError:
                            print("Opción no valida.\nIngresa el Id del Digipymon.")                               
            else:
                    
                print("No tienes ese objeto")

def consultar_inventario(self):
    exit = True
    while exit:
        print(self.bolsa.objetos)
        exit = False

def consultar_digipymons(self):
    exit_guarderia = True
    while exit_guarderia:
        self.jugador1.consultar_digipymons
        exit_guarderia = False






def historia(self):
        print("Un dia  decidiste conquistar el mundo de los digipymon para ello,  ")
        print("te embarcaste en una gran aventura  ")
        nombre_jugador = input("Dinos tu nombre ")
        self.jugador1.nombre = nombre_jugador
        
        
        self.bolsa.añadir_objeto("energetica",1)
        self.bolsa.añadir_objeto("Digipyball",3)
        print("empiezas con una energetica y 3 digiballs")
        self.digipymon = self.generar_digipymon_aleatorio()
        print("este es tu digipymon inicial ")
        self.jugador1.añadir_digipymon(self.digipymon)
        print(f"{self.jugador1.nombre} ha añadido a {self.digipymon.nombre} a su ejercito")
        print(self.digipymon)

def main(self):
        
        
        self.historia()
        

    
        salir =True
        while salir:   
            opcion = self.menu()
            if opcion == 1:
                self.buscar_digipymon()
            if opcion == 2:
                self.combate()   
            if opcion == 3:
                self.digishop()
            elif opcion == 4: 
                self.usar_item()
            elif opcion == 5: 
                self.Consultar_inventario() 
            elif opcion == 6: 
                self.Consultar_digipymons()
            elif opcion == 7: 
                print("saliendo del programa")
                salir = False
                

if __name__==    "__main__":
    videojuego = Main()
    videojuego.main()
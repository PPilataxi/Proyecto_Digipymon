from digipymon import Digipymon
from enemigo import Enemigo
from inventario import Inventario
from jugador import Jugador
from listanombres import ListaNombres
import random

class Main: 
    def __init__(self):
        self.jugador1 = Jugador(None)
        self.bolsa = Inventario()
        self.nombre_digipymon = ListaNombres()
        self.digipymon = None
        self.soldado_enemigo = None
        self.id_contador = 1


    def menu(self):
        
        print("*****¿Qué desea hacer?*****")
        print("1. Buscar digipymon")
        print("2. Luchar contra un entrenador")
        print("3. Ir a la tienda")
        print("4. Usar Objetos")
        print("5. Consultar inventario")
        print("6. Consultar digipymons")
        print("7. Salir")
        
        eleccion =int(input())
        if 1 <= eleccion <= 7:
            return eleccion
        else:
            print("ERROR, no existe esa opción. Ingrese una opción correcta")
        return self.menu()     
        
    def generar_digipymon_aleatorio(self):
            
            
            nombre = self.nombre_digipymon.obtener_nombre_digipymon()
            lista_tipo = ["fuego","agua","planta"]    
            
            vida = random.randint(10, 20)
            ataque = random.randint(1, 10)
            nivel = random.randint(1, 3)
            tipo = random.choice(lista_tipo)
            digipymon=Digipymon( self.id_contador,nombre,vida,ataque,tipo,nivel)
            self.id_contador += 1
            return digipymon 

            #self.digipymon = Digipymon(self.nombre,self.vida,self.ataque,self.tipo,self.nivel)
            #self.añadir_digipymon(self.digipymon)
            
        




    def buscar_digipymon(self):
        
        self.digipymon =self.generar_digipymon_aleatorio()
        
    #Introducción a la función
        print("******Es la hora de buscar digipymons******")
        
        print(f"¡OMFG, {self.digipymon} apareció para torturarte!")
            
         
    #Probabilidad de capturar el digipyball
        captura_porcentaje= max(0, 100 - (self.digipymon.nivel * 10))
        print(f"Tienes un {captura_porcentaje}% de posibilidades de llevarte este digipymon")

    #Decisión de captura
        while True:
            si_no = input("¿Quiéres intentar atraparlo con tus digibolas ;) (si/no)? ").lower()
            print(self.bolsa.objetos )
            if si_no == "si":      
                if "Digipyball" in self.bolsa.objetos and self.bolsa.objetos["Digipyball"] > 0:
                    if self.jugador1.cantidad_digipymon < 6:
                        self.bolsa.usar_objeto("Digipyball") 
                        print(self.bolsa.objetos )
                        if random.randint(1,100) <= captura_porcentaje:
                            print(f"Lograste capturar a este digipymon {self.digipymon.nombre}, Felicidades, era muy dificil")
                            self.jugador1.añadir_digipymon(self.digipymon)

                            break
                        else:
                            print(f"¡¿Como se te puede haber escapado {self.digipymon.nombre}?! Afina la punteria Broh...")
                            break
                    else:
                        print("Tienes todo tu ejercito completo")
                        break
                else:
                    print("¿No te has dado cuenta de que no tienes Digyballs? COMPRA YA CARAJO!!!")
                    break
            elif si_no == "no":
                print("Le tuviste miedo al exito e hiciste bomba de humo frente al digipymon")
                break
            else:
                print("O no sabes leer, o no sabes escribir, ponga si o no por favor.")


    """
    Función combate el cual comprueba si disponemos de digipymons, luego pregunta si queremos combatir
    y hace que tengamos un combate contra una persona con la misma cantidad de digipymons, y tendremos un combate
    en el cual se comparan los puntos de ataque y se resta la vida.
    """
    def combate(self):
        if not self.jugador1.lista_digipymon:
            print("No dispones de ejercito para luchar por la República")
            return
        self.soldado_enemigo = self.generar_digipymon_aleatorio()
        nombre_rival = self.nombre_digipymon.obtener_nombre_entrenador()
        rival = Enemigo(nombre_rival)
        print(f"OMG, apareció {rival.nombre} y se quiere hacer un 1pa1 contra tí.")

        for _ in range(self.jugador1.cantidad_digipymon):
            rival.añadir_digipymon(self.soldado_enemigo)

        print(f"{rival.nombre} tiene reclutado a los siguientes Digipymons")
        for i, soldado_enemigo in enumerate(rival.lista_digipymon):
            print(f"{i + 1 }. {soldado_enemigo.nombre} (Vida: {soldado_enemigo.vida}, Ataque: {soldado_enemigo.ataque})")

        while True:
            pelea = input("¿Desea enfrentarse en el 1 vs 1 ? (si/no)").lower()
            if pelea == "si":
                print("*-*-*-*-* HORA DEL COMBATE *-*-*-*-*")
                i = 0
                j = 0
                while i < len(self.jugador1.lista_digipymon) and j < len(rival.lista_digipymon):
                    mi_soldado = self.jugador1.lista_digipymon[i]
                    soldado_enemigo = rival.lista_digipymon[j]
                    print(f"\n--- Combate {i+1} vs {j+1} ---")
                    print(f"Tu {mi_soldado.nombre} (Ataque: {mi_soldado.ataque}, Vida: {mi_soldado.vida}) vs. {soldado_enemigo.nombre} (Ataque: {soldado_enemigo.ataque}, Vida: {soldado_enemigo.vida})")

                    if mi_soldado.ataque > soldado_enemigo.ataque:
                        diferencia_ataque = mi_soldado.ataque - soldado_enemigo.ataque
                        mi_soldado.vida -= diferencia_ataque
                        print(f"¨{mi_soldado.nombre} va a atacar! {mi_soldado.nombre} ha perdido {diferencia_ataque} de vida. Se ha quedado la siguiente vida: {mi_soldado.vida}")
                        if mi_soldado.vida <= 0:
                            print(f"Ooooh Nooo! {mi_soldado.nombre} ha sido derrotado!")
                            i +=1
                        else:
                            print(f"Tu {mi_soldado.nombre} podrá seguir luchando.")
                            j += 1 

                    elif mi_soldado.ataque < soldado_enemigo.ataque:
                        diferencia_ataque = soldado_enemigo.ataque - mi_soldado.ataque
                        soldado_enemigo.vida -= diferencia_ataque
                        print(f"¡{soldado_enemigo.nombre} va a atacar! {soldado_enemigo.nombre} ha perdido {diferencia_ataque} de vida. (Nueva vida: {soldado_enemigo.vida})")
                        if soldado_enemigo.vida <= 0:
                            print(f"¡{soldado_enemigo.nombre} ha sido derrotado!")
                            j += 1
                        else:
                            print(f"{soldado_enemigo.nombre} puede seguir luchando")

                    else:
                        print("Empate técnico. Ambos digipymons perderán 1 punto de vida")
                        mi_soldado.vida -= 1
                        soldado_enemigo.vida -= 1
                        if mi_soldado.vida <= 0:
                            print(f"Ooooh Nooo! {mi_soldado.nombre} ha sido derrotado!")
                            i +=1
                        if soldado_enemigo.vida <= 0:
                            print(f"¡{soldado_enemigo.nombre} ha sido derrotado!")
                            j += 1
                        else:
                            i += 1
                            j += 1

                print("*-*-*-*-* RESULTADOS DEL COMBATE *-*-*-*-*")
                if i == len(self.jugador1.lista_digipymon) and j < len(rival.lista_digipymon):
                        print("¡Has perdido la Guerra!")
                        self.jugador1.digicoins = max(0, self.jugador1.digicoins - len(rival.lista_digipymon))
                elif j == len(rival.lista_digipymon) and i < len(self.jugador1.lista_digipymon):
                    print("¡Genial, lograste la Victoria!")
                    self.jugador1.digicoins += len(self.jugador1.lista_digipymon)
                else:
                    print("Como se diria el empate en ajedrez. TABLAS.")
                break

            elif pelea == "no":
                if self.jugador1.digicoins > 0:
                    self.jugador1.digicoins -= 1
                    print("Aqui somos como el estado español, hagas lo que hagas te quitamos 1 Digicoin")
                else:
                    print("No dispones de digicoins, asi que lo pagarás con la batalla")
                break
            else:
                print("Por favor, escriba 'si' o 'no'")



    def digishop(self ):
            
        salir_tienda = True
        while salir_tienda: 
            print("*****Bienvenido a la digishop*****")
            print("*****¿Qué desea comprar?*****")
            print("a. Digipyballs: 5 digicoins")
            print("b. Energetica: 3 digicoins (+ 10p digisalud)")
            print("c. Trembolóna: 4 digicoins (+5p de aura )")
            self.jugador1.consultar_digicoins()
            
            
            opcion = input() 
            if opcion == "a" :
                if self.jugador1.digicoins < 5:
                    print("no tienes fondos")
                    
                    

                else:      
                    self.bolsa.añadir_objeto("Digipyball",1)
                    print(self.bolsa.objetos)
                    
                    compra1 =self.jugador1.digicoins - 5
                    self.jugador1.digicoins = compra1
                    self.jugador1.consultar_digicoins()
                    print("se ha añadido al inventario")
                    print("que quieres hacer ahora ")
                    tienda = int(int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) )
                    if tienda == 2 :
                        print("estas saliendo de la tienda ")
                        salir_tienda = False 
                                        

                    elif self.jugador1.digicoins == 0:
                    
                        print("no tienes fondos")
                    
                    
            
                
            elif opcion == "b" :
                if self.jugador1.digicoins < 3:
                    print("no tienes fondos")
                    salir_tienda = False
                    
                else:    
                    self.bolsa.añadir_objeto("energetica",1)
                    print(self.bolsa.objetos)
                    
                    compra2 =self.jugador1.digicoins - 3
                    self.jugador1.digicoins = compra2
                    self.jugador1.consultar_digicoins()
                    print("se ha añadido al inventario")
                    print("que quieres hacer ahora ")
                    tienda = int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) 
                    if tienda == 1 :
                        self.digishop()
                    elif tienda == 2 :
                        print("estas saliendo de la tienda ")
                        salir_tienda = False 
                        

                    elif self.jugador1.digicoins == 0:
                    
                        print("no tienes fondos")
                    
                        salir_tienda = False
            elif opcion == "c" :
                if self.jugador1.digicoins < 4:
                    print("no tienes fondos")
                    salir_tienda = False
                    
                else:    
                    self.bolsa.añadir_objeto("Trembolona",1)
                    print(self.bolsa.objetos)
                    
                    compra3 =self.jugador1.digicoins - 4
                    self.jugador1.digicoins = compra3
                    self.jugador1.consultar_digicoins()
                    print("se ha añadido al inventario")
                    print("que quieres hacer ahora ")
                    tienda = int(input("pulsa 1 para seguir comprando o pulsa 2 para salir de la tienda ") ) 
                    if  tienda == 2 :
                        print("estas saliendo de la tienda ")
                        salir_tienda = False 
                            

                    elif self.jugador1.digicoins == 0:
                        
                        print("no tienes fondos")
                    
                    
            elif opcion == "d" :
                        
                salir_tienda = False 


    def usar_item(self):
            
            
            salir_items = True
            while salir_items:
                
            
                print(f"Que item quieres usar?\n {self.bolsa.objetos} \n 1. Digipyball\n 2. energica\n 3. Trembolona\n 4. Salir")
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
                                                
                                        print(f"{self.digipymon.nombre} gana 10 de salud ")
                                                
                                        print(f"{self.digipymon.nombre} ahora tiene {self.digipymon.vida} puntos de vida.")
                                        self.bolsa.usar_objeto("energetica") 
                                        break
                                    elif respuesta_digi == "salir":
                                        salir_items = False
                                except ValueError:
                                    print("Opción no valida.\nIngresa el Id del Digipymon.")   
                elif respuesta_items == 3 :
                    if "Trembolona"in self.bolsa.objetos:
                            
                            respuesta_digi = int(input(f"Sobre que digipymon quieres usar la Trembolona {self.jugador1.consultar_digipymon()}?\n (escribe el Id o 'salir') "))
                            for digipymon in self.jugador1.lista_digipymon:
                                try:
                                    if  self.digipymon.id == respuesta_digi:                        
                                        self.digipymon.vida += 10
                                        print(f"Le das la Trembolona a {self.digipymon.nombre} ") 
                                                
                                        print(f"{self.digipymon.nombre} gana 5 de ataque ")
                                                
                                        print(f"{self.digipymon.nombre} ahora tiene {self.digipymon.vida} puntos de ataque.")
                                        self.bolsa.usar_objeto("Trembolona") 
                                        break
                                    elif respuesta_digi == "salir":
                                        salir_items = False
                                except ValueError:
                                    print("Opción no valida.\nIngresa el Id del Digipymon.")                                               
                else:
                            
                        print("No tienes ese objeto")


    """
    Función consultar el inventario actual de nuestro jugador donde hay un bucle while que mantiene al jugador dentro
    del inventario hasta que finalice los objetos que tiene el jugador.
    """
    def Consultar_inventario(self):
        exit =True
        while exit: 
            print(self.bolsa.objetos)
            print(self.jugador1.consultar_digicoins())
            exit = False

    """
    Función consultar digipymons, un while que cuando termine de consultar los digipymons
    que están en la lista del jugador(osea el objeto), salga del consultar.
    """
    def Consultar_digipymons(self):
        exit_guarderia = True
        while exit_guarderia: 
            self.jugador1.consultar_digipymon()

            exit_guarderia = False

    """
    Función historia, se ha creado esta función para opcimicación del código en el main y que 
    se pueda ver claramente el main
    """
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

    """
    Función main en la cual llamamon a la historia y hacemos que el menu pueda
    ser interactuado y elegir la opción que sea conveniente para el juego y lo que queramos hacer
    """
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
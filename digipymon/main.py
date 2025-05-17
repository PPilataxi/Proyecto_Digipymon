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
        self.lista_digipymon = ListaNombres()
        self.doyi = None
        
    def historia(self):
        
        nombre_jugador = input("Dinos tu nombre ")
        self.jugador1.nombre = nombre_jugador
        
        print("Un dia  decidiste conquistar el mundo de los digipymon para ello,  ")
        print("te embarcaste en una gran aventura  ")
        self.bolsa.añadir_objeto("energetica",1)
        self.bolsa.añadir_objeto("Digipyball",3)
        print("empiezas con una energetica y 3 digiballs")

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
        return eleccion       
        
    def generar_digipymon_aleatorio(self):
            
            
            nombre = self.obtener_nombre_digipymon()
            lista_tipo = ["fuego","agua","planta"]    

            vida = random.randint(10, 20)
            ataque = random.randint(1, 10)
            nivel = random.randint(1, 3)
            tipo = random.choice(lista_tipo)

            self.doyi = Digipymon(nombre,vida,ataque,tipo,nivel)
            self.añadir_digipymon(self.doyi)
            
        




    def buscar_digipymon(self):
        
        self.el_rebelde =self.generar_digipymon_aleatorio()
    #Introducción a la función
        print("******Es la hora de buscar digipymons******")
        
        print(f"¡OMFG, {self.el_rebelde} apareció para torturarte!")

    #Probabilidad de capturar el digipyball
        captura_porcentaje= max(0, 100 - (self.el_rebelde.nivel * 10))
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
                            print(f"Lograste capturar a este digipymon {self.el_rebelde.nombre}, Felicidades, era muy dificil")
                            self.jugador1.añadir_digipymon(self.el_rebelde)
                            break
                        else:
                            print(f"¡¿Como se te puede haber escapado {self.el_rebelde.nombre}?! Afina la punteria Broh...")
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


    def combate(self):
        if not self.jugador1.lista_digipymon:
            print("No dispones de ejercito para luchar por la República")
            return
        
        nombre_rival = self.obtener_nombre_entrenadores()
        rival = Enemigo(nombre_rival)
        print(f"OMG, apareció {rival.nombre} y se quiere hacer un 1pa1 contra tí.")

        for x in range(self.jugador1.cantidad_digipymon):
            rival.añadir_digipymon(self.generar_digipymon_aleatorio(self.lista_digipymon))

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
                for i in range(min(len(self.jugador1.lista_digipymon, ), len(rival.lista_digipymon))):
                    mi_soldado = self.jugador1.lista_digipymon[i]
                    soldado_rival = rival.lista_digipymon[i]
                    print(f" ----- COMBATE -----")
                    print(f"Va combatir {mi_soldado.nombre} (Vida: {mi_soldado.vida}, Ataque: {mi_soldado.ataque}) ***** VS ***** {soldado_rival.nombre} (Vida: {soldado_rival.vida} Ataque: {soldado_rival.ataque})")




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
            

            
            print(self.bolsa.objetos )
            print("Que item deseas usar ?")
            num2 = int(input("Pulsa 1 para usar energetica " \
                            "2 para usar trembolona  "\
                            "3 para intentar darle una  digiball al digipymon  " ))
            
            
            if num2 == 1:
            
                print("Quieres usar  energetica")
                print("¿En que digipymon deseas usarlo?")
                num1 = int(input("Pulsa 1 para usarlo en self.doyi " \
                                "2 para usarlo en yaya " ))
                
                
                if num1 == 1:
                    print("Quieres usarlo en  " + self.doyi.nombre) 
                    energetica = self.doyi.vida + 10   
                    self.doyi.vida = energetica
                    print( "la vida de self.doyi ahora es : " + str(self.doyi.vida)  )
                    self.bolsa.usar_objeto("energetica")
                    print(self.bolsa.objetos)
                    self.menu()
            elif num2 == 2:

                print("Quieres usar  trembolona")
                print("¿En que digipymon deseas usarlo?")
                num1 = int(input("Pulsa 1 para usarlo en "+ self.doyi.nombre ,
                            "2 para usarlo en " + self.el_rebelde.nombre ))
                if num1 == 1:
                    print("Quieres usarlo en  self.doyi") 
                    tembolona = self.doyi.ataque + 5   
                    self.doyi.ataque =tembolona
                    print(  " el ataque de self.doyi ahora "+ str(self.doyi.ataque) )    
                    self.bolsa.usar_objeto("trembolona")
                    print(self.bolsa.objetos)
                    self.menu()
            elif num2 == 3:

                print("Quieres  intentar darle una  digiball al digipymon  ")
                print("el digipymon se queda mirando la digiball  , tras 5 minutos la cojes para que pueda centrarse en el combate ")
                

    def Consultar_inventario(self):
        exit =True
        while exit: 
            print(self.bolsa.objetos)
            exit = False

    def Consultar_digipymons(self):
        exit_guarderia = True
        while exit_guarderia: 
            self.jugador1.consultar_digipymon(self.digipymon)
            #print("digipymon1: " + self.doyi.nombre ,"digipymon1: " + self.el_rebelde.nombre )
            exit_guarderia = False
        

    def main(self):
        
        
        self.historia()
        
      
    #print(self.jugador1)
        print("este es tu digipymon inicial ")
    #print(" nombre: " + self.doyi.nombre , " vida: " + str(self.doyi.vida) , " ataque: "+ str(self.doyi.ataque) , " tipo: "+ self.doyi.tipo , " nivel: "+ str(self.doyi.nivel))
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
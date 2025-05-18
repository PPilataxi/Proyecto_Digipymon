"""
Esta clase es el inventario que almacena los objetos que puede usar el jugador y que pueden usar los digipymon 
"""
class Inventario():
    
    def __init__(self):
       self.objetos =  {}
    """
    Este metodo comprueba si el objeto esta en eldiccionario objetos si no esta  añade el objeto al diccionario objetos 
    y si esta  incremetna su cantidad  tiene como parametros el nombre del objeto y la cantidad del objeto 
    """
    def añadir_objeto(self,nombre , cantidad ):
        
        if nombre in self.objetos:
            print(f'El objeto {nombre} esta en el inventario y  tienes {self.objetos[nombre]} unidades')
            mas =  self.objetos[nombre] + 1  
            self.objetos.update({nombre:mas})

        else:
            print(f'{nombre} no esta en el inventario')
            print(f'{nombre} se añadira al inventario')
            self.objetos.update({nombre:cantidad})


 
    """
    Este metodo sirve para que eljugador pueda darle objetos al digipymon 
    para ello comprueba si el objeto existe el diccionario objetos ,si existe le resta 1 a la cantidad del objeto y si la cantidad llega a 0 lo elimina del inventario 
    Si no tienes el objeto en tu inventario te avisa con un print de que no tienes ese objeto 
    """
    def usar_objeto(self,objeto):
        
         if objeto in self.objetos:
       
           self.objetos[objeto] -= 1  
           print(f"has usado {objeto}.quedan {self.objetos[objeto]} unidades")

           if self.objetos[objeto] == 0:
                del self.objetos[objeto]
                print (f"el objeto {objeto} se ha eliminado del inventario") 

         else:
            print(f"No dispones {objeto} entre tus objetos personales COMPRAAAA, VIVA EL CAPITALISMO")
     
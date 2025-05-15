class Inventario():
    
    def __init__(self):
       self.objetos =  {}
   
    def añadir_objeto(self,nombre , cantidad ):
        
        if nombre in self.objetos:
            print(f'El objeto {nombre} esta en el inventario y  tienes {self.objetos[nombre]} unidades')
            mas =  self.objetos[nombre] + 1  
            self.objetos.update({nombre:mas})

        else:
            print(f'{nombre} no esta en el inventario')
            print(f'{nombre} se añadira al inventario')
            self.objetos.update({nombre:cantidad})


    def usar_objeto(self,objeto):
        
        
        if {self.objetos[objeto]} < 0:
           menos = {self.objetos[objeto]}  - 1  
        elif menos == 0:
            del(self.objetos[objeto])
            return self.objetos

        else:
            print(f"No dispones {objeto} entre tus objetos personales COMPRAAAA, VIVA EL CAPITALISMO")
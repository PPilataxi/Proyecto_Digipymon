class Inventario():
    
    def __init__(self):
       self.objetos =  {}
   
    def añadir_objeto(self,nombre , cantidad ):
        
        if nombre in self.objetos:
            print(f'El objeto {nombre} esta en el inventario y  tienes {self.objetos[nombre]} unidades')
            mas =  self.objetos[nombre] + 1  
            self.objetos.update({nombre:mas})

        else:
            print(f'{nombre} no esta en la objetos')
            self.objetos.update({nombre:cantidad})


    def usar_objeto(self,objeto):
        cantidad = cantidad
        self.objetos = self.objetos
        if cantidad < 0:
           menos =   - 1  
        else: cantidad = 0
        del(self.objetos["naranja"])
        return self.objetos

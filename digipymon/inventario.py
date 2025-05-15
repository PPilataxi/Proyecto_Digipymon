class Inventario():
    
    def __init__(self):
       self.objetos =  {}
   
    def añadir_objeto(self,nombre , cantidad ):
        
        if nombre in self.objetos:
            print(f'El nombre {nombre} esta y el valor asociado es {self.objetos[nombre]}')
            mas =  self.objetos[nombre] + 1  
            self.objetos.update({nombre:mas})

        else:
            print(f'{nombre} no esta en la objetos')
            self.objetos.update({nombre:cantidad})


    def usar_objeto(self):
        cantidad = cantidad
        self.objetos = self.objetos
        if cantidad < 0:
           cantidad - 1
        else: cantidad = 0
        del(self.objetos["naranja"])
        return self.objetos

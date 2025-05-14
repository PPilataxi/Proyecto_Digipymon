class Inventario():
    
    def __init__(self,objetos):
       self.objetos =  {}
   
    def añadir_objeto(self,nombre , cantidad ):
        nombre = nombre
        cantidad = cantidad
        if nombre in self.objetos:
            print(f'El nombre {nombre} esta y el valor asociado es {self.objetos[cantidad]} ')
            cantidad += 1 
            self.objetos.update({cantidad})

        else:
            print(f'{nombre} no esta en la objetos')
            self.objetos.update({nombre:cantidad})


    def usar_objeto(self):
        cantidad = 1
        self.objetos = {"patata" : 1,"naranja": 2,"manzana": 3}
        if cantidad < 0:
           cantidad - 1
        else: cantidad = 0
        del(self.objetos["naranja"])
        return self.objetos

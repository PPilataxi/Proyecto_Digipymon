class Inventario():
    
    def __init__(self,objetos):
        self.objetos = {"patata" : 1,"naranja": 2}

   
    def añadir_objeto(self,nombre , cantidad ):
        nombre = "patata"
        cantidad = 1
        if nombre in self.objetos:
            print(f'Clave {nombre} esta y el valor asociado es {self.objetos[cantidad]} ')
        else:
            print(f'{nombre} no esta en la objetos')



    def usar_objeto(self):
        self.objetos = {"patata" : 1,"naranja": 2}
        del(self.objetos["naranja"])
        self.objetos
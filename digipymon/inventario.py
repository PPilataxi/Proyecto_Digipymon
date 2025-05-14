class Inventario():
    
    def __init__(self):
       self.objetos =  {}
   
    def añadir_objeto(self,nombre , cantidad ):
        nombre = "patata"
        cantidad = 1
        if nombre in self.objetos:
            print(f'Clave {nombre} esta y el valor asociado es {self.objetos[cantidad]} ')
        else:
            print(f'{nombre} no esta en la objetos')
            self.objetos.update(nombre,cantidad)


    def usar_objeto(self):
        self.objetos = {"patata" : 1,"naranja": 2}
        del(self.objetos["naranja"])
        self.objetos

bolsa = Inventario(objetos = {})
bolsa.añadir_objeto("patata" , 1)
print(bolsa)
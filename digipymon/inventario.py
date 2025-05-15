class Inventario():
    
    def __init__(self,):
        self.objetos =  {}

    def añadir_objeto(self,nombre , cantidad ):
        if nombre in self.objetos:
            self.objetos[nombre] += cantidad
        else:
            self.objetos[nombre]= cantidad
            
    def usar_objeto(self, nombre_objeto):
        if nombre_objeto in self.objetos:
            self.objetos[nombre_objeto] -=1
            if self.objetos[nombre_objeto] == 0:
                del self.objetos [nombre_objeto]
        else:
            print(f"No dispones {nombre_objeto} entre tus objetos personales COMPRAAAA, VIVA EL CAPITALISMO")
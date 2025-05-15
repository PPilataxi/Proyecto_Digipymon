class Jugador():
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10

#Creación método para añadir digipymons
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digypymon += 1
        print(f"{self.nombre} ha añadido a {digipymon} a su ejercito")

#Creación método para consultar los digipymons que tenemos en nuestra posesión
    def consultar_digipymon(self):
        if self.lista_digipymon:
            for digypymon in self.lista_digipymon:
                print(f"Estos son tus digipymon: {digypymon}")
        else:
            print("Aún no tiene ningún digipymon en su colección, VE A CAPTURAR")



#Consultar digicoins
    def consultar_digicoins(self):
        print(f"{self.nombre} tiene en su posesión {self.digicoins} digicoins")

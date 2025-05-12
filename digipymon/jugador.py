class Jugador:
#Creación de métodos por parámetros
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digypymon = 0
        self.digicoins = 10

#Creación método para añadir digipymons
    def añadir_digipymon(self, digipymon):
        self.lista_digipymon.append(digipymon)
        self.cantidad_digypymon += 1
        print(f"{self.nombre} ha añadido a {digipymon} a su ejercito")

#Creación método para consultar los digipymons que tenemos en nuestra posesión
    def consultar_digipymon(self):
            for digypymon in self.lista_digipymon:
                 print("Estos son tus digipymon: " + digypymon)


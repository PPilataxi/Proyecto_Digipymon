"""
Esta clase tiene los atributos de los digipymon y tiene un metodo toString 
"""
class Digipymon():
    def __init__(self,id,nombre,vida,ataque,tipo,nivel):
        self.id = id
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel



    """
    Este metodo es el toString de la clase digipymon recibe self como atributo  al imprimir  el objeto de la clase llama al str y lo imprime 
    retorna el tostring del digipimon
    """     
    def __str__(self):
        return f" ID: {self.id} Nombre: {self.nombre}   , Vida: {self.vida} , Ataque: {self.ataque} , Tipo :{self.tipo}  , Nivel: {self.nivel}" 
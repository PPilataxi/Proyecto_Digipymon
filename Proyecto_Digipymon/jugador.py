

class Jugador():
  """
  Representa a un jugador en el juego.

  Atributos:
  ----------
  - nombre : str  
  Nombre del jugador.  

  - lista_digipymon : list  
  Diccionario vacío donde se guardan los digipymons del jugador.  

  - cantidad_digipymon : int  
  Número de digipymons en la lista (inicializado en 0).  

  - digicoins : int  
  Monedas del juego, inicializadas en 10.  

  Este objeto permite al jugador interactuar con el programa.

  """
  def __init__(self, nombre):

        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0
        self.digicoins = 10
 

  def añadir_digipymon(self, digipymon):
        """
        Añade un digipymon a la lista de digipymons del jugador.

        Parámetros:
        ----------
        - digipymon : object  
        El digipymon a añadir.

        Este método usa `append` para añadir el digipymon y aumenta `cantidad_digipymon` en 1.

        """   
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
        


  def consultar_digipymon(self):
        """
        Consulta los digipymons que tiene el jugador.

        Si la lista de digipymons **no está vacía**, imprime cada digipymon.  
        Si está vacía, muestra un mensaje indicando que el jugador aún no tiene digipymons.

        """
        if self.lista_digipymon:
            for digipymon in self.lista_digipymon:
                 print (f"Estos son tus digipymon: {digipymon}" )
                
        else:
            print(f"{self.nombre} aún no tiene ningún digipymon en su colección")




  def consultar_digicoins(self):
         """
        Consulta la cantidad de digicoins que tiene el jugador.

        Muestra el nombre del jugador junto con la cantidad de digicoins que posee.

        """
         print(f"{self.nombre} tiene en su posesión {self.digicoins} digicoins")



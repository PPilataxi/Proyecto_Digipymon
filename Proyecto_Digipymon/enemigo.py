

class Enemigo():
    """
  Clase que representa a un enemigo en el juego.

  Atributos:
  ----------
  - nombre : str  
    Nombre del enemigo.  
  - lista_digipymon : list  
    Lista de digipymons asociados al enemigo.  
  - cantidad_digipymon : int  
    Cantidad de digipymons en la lista (inicializado en 0).  

  Esta clase permite que el enemigo pueda enfrentarse con el jugador.

  """
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_digipymon = []
        self.cantidad_digipymon = 0

  
    def añadir_digipymon(self, digipymon):
        """
        Añade un digipymon a la lista de digipymons del enemigo.

        Parámetros:
        ----------
        - digipymon : object  
        El digipymon a añadir.

        Este método usa `append` para añadir el digipymon y aumenta `cantidad_digipymon` en 1.

        """
        self.lista_digipymon.append(digipymon)
        self.cantidad_digipymon += 1
       
      

   
        
                       


import os
import os.path
class Servicio_Peliculas:
    
    def __init__(self):
       self.nombre_archivo = "peliculas.txt"
    
    def agregar_pelicula(self, pelicula):
        with open(self.nombre_archivo, "a",encoding='utf8') as archivo:
            archivo.write(f'{pelicula}\n')
            
    def listar_peliculas(self):
        try:
            with open(self.nombre_archivo, "r",encoding='utf8') as archivo:
                print("--- Listado de peliculas ---")
                print(archivo.read())
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return []
        
    def eliminar_pelicula(self):
        os.remove(self.nombre_archivo)
        print(f"Archivo {self.nombre_archivo} eliminado.")
        
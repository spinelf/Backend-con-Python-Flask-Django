from Catalogo_de_peliculas.servicio_peliculas import Servicio_Peliculas
from Catalogo_de_peliculas.pelicula import Pelicula 

class AppCatalogoPeliculas:
    
    def __init__(self):
        self.servicio_peliculas = Servicio_Peliculas()
    
    def mostrar_menu(self):
        print("Bienvenido al catálogo de películas")
        
        while True:
            try:
                print(f'''Opciones:
                      1. Agregar película
                      2. Listar películas
                      3. Eliminar catalogo de películas
                      4. Salir''')
                opcion = int(input("Seleccione una opción: "))
                if opcion==1:
                    nombre_pelicula = input("Ingrese el nombre de la película: ")
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_pelicula(pelicula)
                    print(f"Película '{nombre_pelicula}' agregada al catálogo.")
                elif opcion==2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion==3:
                    self.servicio_peliculas.eliminar_pelicula()
                elif opcion==4:
                    print("Salimos del catálogo de películas.")
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")
            except ValueError:
                print("Opción no válida. Por favor, elige una opción válida.")
            
            except Exception as e:
                print(f"Ocurrio un error: {e}")
    
    
if __name__ == "__main__":
    app = AppCatalogoPeliculas()
    app.mostrar_menu()
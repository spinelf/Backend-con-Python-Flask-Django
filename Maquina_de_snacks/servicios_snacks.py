import os.path
from Maquina_de_snacks.snack import Snack

class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snack.txt'
    
    def __init__(self):
        self.snacks = []
        # Revisar si ya existe el archivo de snacks
        # Si ya existe obtenemos los snacks del archivo y sino existe cargamos algunos snack iniciales.
        
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        else:
            self.cargar_snacks_iniciales()
    
    def cargar_snacks_iniciales(self):
        snacks_iniciales =[
            Snack('Papas',70),
            Snack('Refresco',50),
            Snack('Sandwich',120)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)
    
    def guardar_snacks_archivo(self,snacks):
        try:
            with open(self.NOMBRE_ARCHIVO,'a') as archivo:
                for snack in snacks:
                    archivo.write(f'{snack.escribir_snack()}\n')
        except Exception as e:
            print(f'Error al guardar snacks en archivo: {e}')
    
    def obtener_snacks():
        pass
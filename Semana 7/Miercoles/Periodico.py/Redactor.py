from faulthandler import cancel_dump_traceback_later
from unicodedata import name
from Articulos import Articulos

class Redactor:
    def __init__(self,name,cedula):
        self.name=name
        self.cedula=cedula
        


    def escribir_articulo(self):
        print('\nestoy escribiendo un articulo')
        articulo= Articulos(
            input('Titulo:'),
            input('Resumen:'),
            input('Cuerpo:'),
            input('Imagenes: '),
            input('fecha publicacion: '),
            input('fecha creacion: '),None
        )
        print('termine de escribir el articulo',articulo.titulo)
        return articulo



    
        
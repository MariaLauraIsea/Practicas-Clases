import random
from Redactor import Redactor

class Jefe(Redactor):
    def __init__(self, name, cedula,redactores):
        super().__init__(name, cedula)
        self.redactores_supervisados=redactores


    def supervisar(self):
        print('todo esta bien')

    def decidir(self,articulo):
        nro=random.random()
        if  nro> 0.5:
            print('el articulo',articulo.titulo,'fue aprobado')
            return True
        else:
            print('el articulo',articulo.titulo,' no fue aprobado')
            return False
        
    
        
from Bebidas import Bebida

class Alcoholica(Bebida):
    def __init__(self, nombre, precio,grado_alcoholico):
        super().__init__(nombre, precio)
        self.grado_alcoholico=grado_alcoholico
        self.type='alcoholica'


    def show(self):
        print(f'\n---{self.nombre}---')
        print('precio: $',self.precio)
        print('grado alcoholico: °',self.grado_alcoholico)

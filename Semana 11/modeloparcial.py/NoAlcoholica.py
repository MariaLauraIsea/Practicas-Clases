from Bebidas import Bebida

class NoAlcoholica(Bebida):
    def __init__(self, nombre, precio,temperatura):
        super().__init__(nombre, precio)
        self.temperatura=temperatura
        self.type='no alcoholica'

    def show(self):
        print(f'\n---{self.nombre}---')
        print('precio: $',self.precio)
        print('temperatura: °',self.temperatura)
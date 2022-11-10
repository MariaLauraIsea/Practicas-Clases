from Alimento import Alimento

class Comida(Alimento):
    def __init__(self, nombre, precio,platillo,sabor):
        super().__init__(nombre, precio)
        self.tipo_platillo=platillo
        self.sabor_platillo=sabor

    def show_attributes(self):
        print('nombre:',self.nombre)
        print('precio:',self.precio)
        print('platillo:',self.tipo_platillo)
        print('sabor:',self.sabor_platillo)

   
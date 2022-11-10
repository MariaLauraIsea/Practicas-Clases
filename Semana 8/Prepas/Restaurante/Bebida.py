from Alimento import Alimento

class Bebida(Alimento):
    def __init__(self, nombre, precio,porcentaje_alcoholico,temperatura):
        super().__init__(nombre, precio)
        self.porcentaje_alcoholico=porcentaje_alcoholico
        self.temperatura=temperatura


    def show_attributes(self):
        print('nombre:',self.nombre)
        print('precio:',self.precio)
        print('porcentaje alcoholico: %',self.porcentaje_alcoholico)
        print('temperatura: °',self.temperatura)
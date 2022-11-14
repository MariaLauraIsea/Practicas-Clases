from Personas import Persona

class Tecnico(Persona):
    def __init__(self, nombre, ci, tiempo_equipo, sueldo,tipo_direccion):
        super().__init__(nombre, ci, tiempo_equipo, sueldo)
        self.tipo_direccion=tipo_direccion

    def show(self):
        print(f'----TECNICO: {self.nombre}----')
        print(' ci:',self.ci)
        print(' años en el equipo:',self.tiempo_equipo)
        print(' sueldo: $',self.sueldo)
        print(' tipo de director:',self.tipo_direccion)

    def ajustar_sueldo(self):
        ajuste=0
        if self.tiempo_equipo>5:
            ajuste=self.sueldo*0.15

        self.sueldo+=ajuste

        print('\n*****se ha ajustado el sueldo de los tecnicos*****')
        self.show()

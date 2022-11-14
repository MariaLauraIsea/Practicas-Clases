from Personas import Persona

class Jugador(Persona):
    def __init__(self, nombre, ci, tiempo_equipo, sueldo,posicion,juego_estrella):
        super().__init__(nombre, ci, tiempo_equipo, sueldo)
        self.posicion=posicion
        self.juego_estrella=juego_estrella

    def show(self):
        print(f'\n----{self.nombre.upper()}----')
        print(' ci:',self.ci)
        print(' años en el equipo:',self.tiempo_equipo)
        print(' sueldo: $',self.sueldo)
        print(' posicion:',self.posicion)
        print(' participo en el juego de las estrellas:',self.juego_estrella)

    def ajustar_sueldo(self):
        ajuste=0
        if self.juego_estrella==True:
            ajuste=self.sueldo*0.12

        self.sueldo+=ajuste
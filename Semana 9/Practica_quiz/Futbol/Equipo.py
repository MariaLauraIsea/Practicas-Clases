from Jugador import Jugador
from Tecnico import Tecnico
class Equipo:
    def __init__(self,jugadores):
        self.jugadores=jugadores


    def recorrer(self,personas):
        print('\n---JUGADORES QUE ASISTIERON AL JUEGO DE LAS ESTRELLAS---')
        for player in self.jugadores:
            player.show()

        for p in personas:
            p.ajustar_sueldo()
        


        

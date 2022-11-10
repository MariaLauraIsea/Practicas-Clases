from Vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, placa, puesto, marca, hora_entrada):
        super().__init__(placa, puesto, marca, hora_entrada)
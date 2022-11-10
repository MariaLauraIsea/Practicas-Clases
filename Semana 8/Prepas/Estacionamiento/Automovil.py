from Vehiculo import Vehiculo

class Automovil(Vehiculo):
    def __init__(self, placa, puesto, marca, hora_entrada,minusvalido):
        super().__init__(placa, puesto, marca, hora_entrada)
        self.minusvalido= minusvalido


    def show_attributes(self):
        print(f'-------{self.placa}------\nPuesto: {self.puesto}\nMarca: {self.marca}\nHora de entrada: {self.hora_entrada}\nEs minusvalido: {self.minusvalido}')
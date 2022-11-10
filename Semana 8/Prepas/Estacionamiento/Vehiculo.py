class Vehiculo:
    def __init__(self,placa,puesto,marca,hora_entrada):
        self.placa=placa
        self.puesto=puesto
        self.marca=marca
        self.hora_entrada=hora_entrada
        self.hora_salida=None


    def show_attributes(self):
        print(f'-------{self.placa}------\nPuesto: {self.puesto}\nMarca: {self.marca}\nHora de entrada: {self.hora_entrada}')
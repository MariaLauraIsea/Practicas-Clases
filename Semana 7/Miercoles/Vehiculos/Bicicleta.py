from Vehiculos import Vehiculos

class Bicicleta(Vehiculos):
    def __init__(self, color, ruedas,tipo):
        super().__init__(color, ruedas)
        self.tipo=tipo


class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
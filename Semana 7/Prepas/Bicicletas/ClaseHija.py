from defobjeto import Bicicleta

class BicicletaKids(Bicicleta):
    def __init__(self, color, asiento, manubrio,rueditas):
        super().__init__(color, asiento, manubrio)
        self.rueditas=rueditas


class BicicletaElectrica(Bicicleta):
    def __init__(self, color, asiento, manubrio,velocidad_max):
        super().__init__(color, asiento,manubrio)
        self.velocidad_max=velocidad_max
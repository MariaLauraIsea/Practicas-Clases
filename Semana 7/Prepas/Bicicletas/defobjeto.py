class Bicicleta:
    
    def __init__(self,color,asiento,manubrio):
        self.color=color
        self.asiento=asiento
        self.manubrio=manubrio


    def identidad(self):
        print(f'color: {self.color}\nmaterial del asiento: {self.asiento}\ntipo de manubrio: {self.manubrio}')

    def extraer(self):
        return {'color':self.color,'material del asiento':self.asiento,'tipo de manubrio':self.manubrio}

    def identidad_color(self):
        identidad_color=self.color
        return identidad_color


    
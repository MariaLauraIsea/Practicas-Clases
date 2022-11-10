from Imagen import Imagen

class Anuncios:
    def __init__(self,imagen,seccion):
        self.seccion=seccion
        self.imagen=imagen



class AnuncioClasificado:
    def __init__(self,precio,fecha_publicacion,dias,tipo):
        self.precio=precio
        self.fecha_publicacion=fecha_publicacion
        self.cantidad_dias=dias
        self.tipo=tipo


class AnuncioClasificadoVehiculo(AnuncioClasificado):
    def __init__(self, precio, fecha_publicacion, dias,marca,modelo,año,color,kilometraje):
        super().__init__(precio, fecha_publicacion, dias,'Vehiculo')
        self.marca=marca
        self.mpdelo=modelo
        self.año=año
        self.color=color
        self.kilometraje=kilometraje


class AnuncioClaificadoVivienda(AnuncioClasificado):
    def __init__(self, precio, fecha_publicacion, dias, m2,cuartos,baños,puesto,politica):
        super().__init__(precio, fecha_publicacion, dias, 'Vivienda')
        self.m2=m2
        self.cuartos=cuartos
        self.baños=baños
        self.puestos=puesto
        self.politica=politica
from Anuncios import Anuncios

class AnuncioClasificado(Anuncios):
    def __init__(self, nombre_publicador, cedula_publicador, seccion, titulo_anuncio, cuerpo_anuncio,precio,fecha_anuncio,dias,producto_vendido):
        super().__init__(nombre_publicador, cedula_publicador, seccion, titulo_anuncio, cuerpo_anuncio)
        self.precio=precio
        self.fecha_anuncio=fecha_anuncio
        self.dias=dias
        self.producto_vendido=producto_vendido



class AnuncioVehiculo(AnuncioClasificado):
    def __init__(self, nombre_publicador, cedula_publicador, seccion, titulo_anuncio, cuerpo_anuncio, precio, fecha_anuncio, dias, producto_vendido,marca,modelo,año,color,kilometraje):
        super().__init__(nombre_publicador, cedula_publicador, seccion, titulo_anuncio, cuerpo_anuncio, precio, fecha_anuncio, dias, producto_vendido)
        self.marca=marca
        self.modelo=modelo
        self.año=año
        self.color=color
        self.kilometraje=kilometraje

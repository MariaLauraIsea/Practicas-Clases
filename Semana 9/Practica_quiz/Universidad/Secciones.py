class Seccion:
    def __init__(self,nombre,codigo,profesor,salon,horario):
        self.nombre=nombre
        self.codigo=codigo
        self.profesor=profesor
        self.salon=salon
        self.horario=horario

    def get_nombre_cod(self):
        print('nombre asignatura:',self.nombre)
        print('codigo asignatura:',self.codigo)
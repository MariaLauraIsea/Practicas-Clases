class Alumno:
    def __init__(self,nombre,grado,promedio,direccion,representante,telefono):
        self.nombre=nombre
        self.grado=grado
        self.promedio=promedio
        self.direccion=direccion
        self.representante=representante
        self.telefono=telefono
        self.becado= 'Si' if promedio >= 18 else 'No'
        
        

    def cap(self):
        return self.nombre.capitalize()


    def show(self):
        print(f'Nombre: {self.nombre}\nGrado: {self.grado}\nPromedio: {self.promedio}\nDireccion: {self.direccion}\nRepresentante: {self.representante}\nTelefono: {self.telefono}\nBecado: {self.becado}')





    
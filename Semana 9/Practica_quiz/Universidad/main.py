from Alumno import Alumno
from Profesor import Profesor
from Secciones import Seccion

#preguntar como hacer para limitar la cantidad de elementos para el atributo de una clase

def agregar_seccion(profesor,seccion):
    secciones_profesor=[]
    secciones_profesor.append(seccion)
    profesor.secciones=secciones_profesor


def main():
    profesor_1=Profesor('sebastian','alameda',13055987)
    seccion_1=Seccion('fisica','AF101',profesor_1,'A112','10:30am')
    agregar_seccion(profesor_1,seccion_1)
    print(profesor_1.nombre)
    for seccion in profesor_1.secciones:
        seccion.get_nombre_cod()

    for seccion in profesor_1.secciones:
        print(seccion.nombre)
        print(seccion.codigo)

    
    

main()
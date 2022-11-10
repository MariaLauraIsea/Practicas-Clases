from Persona import Persona
from Comida import Comida
from Bebida import Bebida

def registrar_comida():
    nombre=input('ingrese el nombre de la comida: ')
    precio=int(input('ingrese el precio del articulo: $'))
    tipo_platillo=input('indique si el platillo es un plato principal o postre: ')
    sabor_platillo=input('indique si la comida es dulce o salada: ')

    return nombre,precio,tipo_platillo,sabor_platillo

def registrar_bebida():
    nombre=input('ingrese el nombre de la comida: ')
    precio=int(input('ingrese el precio del articulo: $'))
    porcentaje_alcoholico=input('indique si el platillo es un plato principal o postre: ')
    temperatura=input('indique si la comida es dulce o salada: ')

    return nombre,precio,porcentaje_alcoholico,temperatura


def registrar_persona():
    nombre=input('ingrese su nombre: ')
    apellido=input('ingrese su apellido: ')
    fecha_nacimiento=input('indique su fecha de nacimiento en formato DD/MM/AAAA: ')
    cedula=input('ingrese su numero de cedula: ')

    return nombre,apellido,fecha_nacimiento,cedula


def main():
    lista_comida=[]
    lista_bebida=[]
    lista_personas=[]
    while True:
        opcion=input('\nQUE DESEA REGISTRAR?\n1-Comida\n2-Bebida\n3-Persona\n4-Mostrar registros\n5-Realizar compra\n6-Salir\n=> ')

        if opcion=='1':
            nombre,precio,tipo_platillo,sabor_platillo=registrar_comida()
            comida=Comida(nombre,precio,tipo_platillo,sabor_platillo)
            lista_comida.append(comida)
            print('\nse ha registrado el alimento con exito!\n')
            comida.show_attributes()

        elif opcion=='2':
            nombre,precio,porcentaje_alcoholico,temperatura=registrar_bebida()
            bebida=Bebida(nombre,precio,porcentaje_alcoholico,temperatura)
            lista_bebida.append(bebida)
            print('\nse ha registrado el alimento con exito!')
            bebida.show_attributes()

        elif opcion=='3':
            nombre,apellido,fecha_nacimiento,cedula=registrar_persona()
            monto_total=0
            persona=Persona(nombre,apellido,fecha_nacimiento,cedula,monto_total)
            lista_personas.append(persona)

        elif opcion=='4':
            print('****COMIDAS REGISTRADAS****')
            for comida in lista_comida:
                print('\n')

                comida.show_attributes()


            print('****BEBIDAS REGISTRADAS****')
            for bebida in lista_bebida:
                print('\n')

                bebida.show_attributes()

        elif opcion=='5':
            alimentos_comprar=[]
            nombre,apellido,fecha_nacimiento,cedula=registrar_persona()
            monto_total=0
            persona=Persona(nombre,apellido,fecha_nacimiento,cedula,monto_total)
            lista_personas.append(persona)
            
            accion=input('seleccione que tipo de alimento desea agregar a su compra:\n1-Comida\n2-Bebida\n=> ')

            if accion=='1':
                print('****COMIDAS REGISTRADAS****')
                for comida in lista_comida:
                    print('\n')

                    comida.show_attributes()

                comida_agregar=input('indique el nombre de la comida que desea adquirir: ')

                for comida in lista_comida:
                    if comida_agregar==comida.nombre:
                        monto_total+=comida.precio



        
        else:
            break



main()
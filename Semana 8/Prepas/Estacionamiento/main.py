from Automovil import Automovil
from Motocicleta import Motocicleta



def registro(vehiculos):
    vehiculos_objetos=[]
    for v in vehiculos:
        if v["type"] == "AUTOMOVIL":
            vehiculo=Automovil(v['placa'],v['puesto'],v['marca'],v['entrada'],v['minusvalido'])
            
        else:
            vehiculo=Motocicleta(v['placa'],v['puesto'],v['marca'],v['entrada'])
            
        vehiculos_objetos.append(vehiculo)
    
    
    return vehiculos_objetos 


def main():
    vehiculos=[ 
    { "type": "AUTOMOVIL", "placa": "ABC12D", "marca": "Chevrolet", "puesto": "A12", "entrada": "10:00:36", "minusvalido": False},
    { "type": "AUTOMOVIL", "placa": "IJK56M", "marca": "Mazda", "puesto": "A33", "entrada": "11:48:22", "minusvalido": False},
    { "type": "MOTOCICLETA", "placa": "EFG34H", "marca": "Suzuki", "puesto": "B10", "entrada": "10:20:15"},
]
    vehiculos_objetos=[]
    vehiculos_objetos=registro(vehiculos)
    
    while True:
        opcion=input('ADMINISTRADOR DE ESTACIONAMIENTO\n1-Entrada\n2-Salida\n3-Ver Estacionamiento\n4-Cerrar programa\n=> ')

        if opcion=='1':
            lleno=True
            for v in vehiculos_objetos:
                if v.puesto==None:
                    lleno=False

            if lleno:
                print('\nEl estacionamiento se encuetra lleno\n')
            else:
                for v in vehiculos_objetos:
                    v.show_attributes()

                choice=input('ingrese la placa del vehiculo que se va ingresar al estacionamiento: ').upper()
                for v in vehiculos_objetos:
                    if choice==v.placa:
                        v.puesto=input('indique el puesto ocupado por el vehiculo: ')
                        

        elif opcion=='2':
            for v in vehiculos_objetos:
                v.show_attributes()

            seleccion=input('ingrese la placa del vehiculo que se va a retirar: ').upper()
            
            for v in vehiculos_objetos:
                if seleccion==v.placa:
                    v.puesto=None
                    v.salida=input('indique la hora de salida del vehiculo: ')
                    print(v.salida)
            
            print('\nel vehiculo ha salido del estacionamiento\n')


        elif opcion=='3':
            print('\n----VEHICULOS EN EL ESTACIONAMIENTO----')
            for v in vehiculos_objetos:
                if v.puesto!=None:
                    v.show_attributes()

        else:
            break

main()
def get_datos():
    cedula=input('por favor ingrese su numero de cedula: ')
    vehiculo=input('seleccione el tipo de vehiculo de su preferencia:\nA - Automatico\nS - Sincronico\n=> ')
    horas=int(input('indique la cantidad de horas de clase que desea tomar: '))
    return cedula,vehiculo,horas


def promedio(total_s,total_a):
    if len(total_s)==0:
        promedio_s=0
    else:
        promedio_s=sum(total_s)/len(total_s)
    if len(total_a)==0:
        promedio_a=0
    else:
        promedio_a=sum(total_a)/len(total_a)
    return promedio_s,promedio_a

def main():
    tarifas=[{'A':2500},{'S':3500}]
    clientes=0
    clientes_s=0
    clientes_a=0
    clientes_discount=0
    total_s=[]
    total_a=[]
    print('Bienvenido a la autoescuela LA RAPIDA')
    
    while True:
        option=int(input('ingrese una opcion para continuar:\n1-Agregar conductor\n2-Mostrar estadisticas\n3-Salir\n=> '))
        if option==1:
            descuento=0
            cedula,vehiculo,horas=get_datos()
            
            
            for tipo in tarifas: 
                costo=tipo.get(vehiculo)
                if costo!=None:
                    break
                
                
            
            #NOMBRE VEHICULO
            if vehiculo=='S':
                nombre_vehiculo='Sincronico'
            else:
                nombre_vehiculo='Automatico'
            
            #DESCUENTO
            if horas>3:
                descuento+=costo*0.15

            #TOTAL
            costo*=horas
            total=costo-descuento

            #FACTURA
            print('\n****FACTURA*****')
            print('cedula - ',cedula)
            print('tipo de vehiculo - ',nombre_vehiculo)
            print('monto total a pagar - $',total)
            print('\n')


            #ESTADISTICAS
            clientes+=1

            if vehiculo=='S':
                clientes_s+=1
            else:
                clientes_a+=1

            if descuento!=0:
                clientes_discount+=1

            if vehiculo=='S':
                total_s.append(total)
            else:
                total_a.append(total)

            promedio_s,promedio_a=promedio(total_s,total_a)

        elif option==2:
            if clientes==0:
                print('\nPor los momentos no hay conductores registrados\n')
            else:
                print('****FINAL DEL DIA****')
                print('total de clientes - ',clientes)
                print('clientes con vehiculo Automatico - ',clientes_a)
                print('clientes con vehiculo Sincronico - ',clientes_s)
                print('clientes con descuento - ',clientes_discount)
                print('Promedio de facturacion para vehiculos Automaticos - ',promedio_a)
                print('Promedio de facturacion para vehiculos Sincronicos - ',promedio_s)
        
        
        else:
            break


main()
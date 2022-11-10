def get_option():
    while True:
        try:
            opcion=int(input('Ingrese una opcion para continuar:\n1-Registrar horas de vuelo\n2-Mostrar estadisticas\n3-Salir\n=> '))
            break
        except:
            print('\ningreso invalido')
    return opcion
    

def get_data():
    cedula=input('por favor ingrese su numero de cedula: ')
    plane_type=input('seleccione el tipo de avion a utilizar:\nH - Helice\nJ - Jet\n=> ')
    horas=int(input('ingrese el numero de horas de vuelo: '))
    return cedula,plane_type,horas


def get_promedio(pilotos_h,pilotos_j):
    if len(pilotos_h)==0:
        promedio_h=0
    else:
        promedio_h=sum(pilotos_h)/len(pilotos_h)

    if len(pilotos_j)==0:
        promedio_j=0
    else:
        promedio_j=sum(pilotos_j)/len(pilotos_j)

    return promedio_j,promedio_h



def main():
    tarifas=[{'J':50},{'H':40}]
    pilotos=[]
    pilotos_j=[]
    pilotos_h=[]
    pilotos_aumento=0




    print('Bienvenido a la base de datos de Saman Airlines')
    while True:
        opcion=get_option()
        if opcion==1:
            cedula,plane_type,horas=get_data()
            

            #PAGO
            for aircraft in tarifas:
                pago=aircraft.get(plane_type)
                if pago!=None:
                    break

            #NOMBRE AVION
            if plane_type=='J':
                plane_name='Jet'
            else:
                plane_name='Helice'
            
            #AUMENTO
            aumento=0
            if horas>8:
                aumento=pago*0.1

            #TOTAL
            pago=pago*horas
            total=pago+aumento

            #DATOS
            print('***DATOS PILOTO***')
            print('cedula: ',cedula)
            print('tipo de avion: ',plane_name)
            print('monto total pago: ', total)
            

            #ESTADISTICAS
            piloto={'cedula':cedula,'tipo de avion':plane_name,'horas de vuelo':horas,'paga':total}
            pilotos.append(piloto)

            if plane_type=='J':
                pilotos_j.append(total)
            else:
                pilotos_h.append(total)

            if aumento!=0:
                pilotos_aumento+=1

            promedio_j,promedio_h=get_promedio(pilotos_h,pilotos_j)


    
        elif opcion==2:
            print('******FINAL DEL DIA******')
            print('cantidad de pilotos:',len(pilotos))
            print('***INFORMACION POR PILOTO***')
            for p in pilotos:
                print('\n')
                for info,data in p.items():
                    print(f'{info} - {data}')

            print('cantidad de pilotos con jet: ',len(pilotos_j))
            print('cantidad de pilotos con helice: ',len(pilotos_h))
            print('cantidad de pilotos con aumento: ',pilotos_aumento)
            print('\n***promedio de pago segun avion***')
            print('Jet: $',round(promedio_j,2))
            print('Helice: $',round(promedio_h,2))


        else:
            break




main()
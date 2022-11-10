
def seleccion_opcion():
    opcion=int(input('\nSelecione una opcion  para continuar:\n1-Agregar Aspirante\n2-Mostrar base de datos\n3-Salir\n=> '))
    return opcion

def bienvenida():
    print('Bienvenido al registro de datos de la Universidad Saman')

def registro_estudiante():
    cedula=input('ingrese su numero de cedula: ')
    promedio=int(input('ingrese su promedio de notas: '))
    infoestudiante={'c.i': cedula,'promedio notas':promedio}

    return infoestudiante

def get_promedio(estudiante):
    for tipodato,datoingresado in estudiante.items():
        if tipodato=='promedio notas':
            promedio=datoingresado
    return promedio


def trimestre_asignado(promedio):
    if promedio>=18:
        trimestre='dos'
        print('su trimestre asignado es el dos')
    elif promedio>=12:
        trimestre='uno'
        print('su trimestre asignado es el uno')
    else:
        trimestre='usted fue rechazado'
        
    return trimestre

def estudiante_trimestre(estudiante,trimestre):
    estudiante['trimestre asignado']=trimestre
    return estudiante

def cantidad_estudiantes(promedio,trimestre,total_alumnos_dos,total_alumnos,total_alumnos_uno,aspirantes):
    if promedio>=12:  
        total_alumnos.append(promedio)
    else:
        aspirantes.append(promedio)

    if trimestre=='uno':
        total_alumnos_uno.append(promedio)
    elif trimestre=='dos':
        total_alumnos_dos.append(promedio)
    else:
        pass
    return total_alumnos,total_alumnos_dos,total_alumnos_uno,aspirantes
    

def get_promedio_total(total_alumnos,total_alumnos_uno,total_alumnos_dos,aspirantes):
    promedio_total=sum(total_alumnos)/len(total_alumnos)
    promedio_1=sum(total_alumnos_uno)/len(total_alumnos_uno)
    promedio_2=sum(total_alumnos_dos)/len(total_alumnos_dos)
    try:
        promedio_aspirantes=sum(aspirantes)/len(aspirantes)
    except ZeroDivisionError:
        promedio_aspirantes=0
        print('no hay estudiantes rechazados para el trimestre en la base de datos')
    return promedio_total,promedio_1,promedio_2,promedio_aspirantes
        
def get_promedio_aspirantes(total_alumnos_cantidad):
    promedio_cantidad_aspirantes=total_alumnos_cantidad/2
    return promedio_cantidad_aspirantes


def main():
    bienvenida()
    quit=False
    total_alumnos=[]
    total_alumnos_uno=[]
    total_alumnos_dos=[]
    aspirantes=[]

    while quit==False:
        opcion=seleccion_opcion()
    
        
        if opcion==1:
            estudiante=registro_estudiante()
            promedio=get_promedio(estudiante)
            trimestre=trimestre_asignado(promedio)
            estudiante_trimestre(estudiante,trimestre)
            total_alumnos,total_alumnos_dos,total_alumnos_uno,aspirantes=cantidad_estudiantes(promedio,trimestre,total_alumnos_dos,total_alumnos,total_alumnos_uno,aspirantes)
    
            total_alumnos_cantidad=len(total_alumnos)
            alumnos_uno=len(total_alumnos_uno)
            alumnos_dos=len(total_alumnos_dos)
            aspirantes_cantidad=len(aspirantes)
            
            
            print('*****INFORMACION DEL ESTUDIANTE*****')
            for key,value in estudiante.items():
                print(f'{key}: {value}')
            

        elif opcion==2:
            promedio_cantidad_aspirantes=get_promedio_aspirantes(total_alumnos_cantidad)
            promedio_total,promedio_1,promedio_2,promedio_aspirantes=get_promedio_total(total_alumnos,total_alumnos_uno,total_alumnos_dos,aspirantes)
            print(f'Cantidad de alumnos total: {total_alumnos_cantidad}')
            print(f'Cantidad de alumnos rechazados: {aspirantes_cantidad} ')
            print(f'****Cantidad de alumnos segun trimestre****\nTrimestre uno: {alumnos_uno}\nTrimestre dos: {alumnos_dos}')
            print(f'Promedio de aspirantes: {promedio_cantidad_aspirantes}')
            print(f'Promedio de notas por cada trimestre:\nPromedio trimestre uno: {promedio_1}\nPromedio trimestre dos: {promedio_2}')
            print(f'\nPromedio general del trimestre: {promedio_total}')
        else:
            quit=True

    




main()
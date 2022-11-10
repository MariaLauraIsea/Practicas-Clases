


def welcome():
    print('bienvenido a tu agenda personalizada!')


def get_option():
    accion=input('1- Agendar nuevo evento\n2- Ver eventos guardados\n3- Salir\n-=> ')
    while accion!='1' and accion!='2' and accion!='3':
        accion=input('ingreso invalido, seleccione una opcion\n1- Agendar nuevo evento\n2- Ver eventos guardados\n=> ')
    return accion

def tomar_nombre():

    nombre_evento=input('indique el nombre del evento a agendar:  ')
    while not nombre_evento.isalpha():
        nombre_evento=input('ingreso invalido. indique el nombre del evento a agendar:  ')

    return nombre_evento


def tomar_fecha(meses,dias,horas):
    print('***seleccione el mes del evento***')
    for mes in meses:
        print(mes)
    mes_seleccionado=input('=> ')
    

    print('***seleccione el dia del evento***')
    if mes_seleccionado.lower=='febrero':
        for dia in range(1,29):
            print (dia)
    elif mes_seleccionado.lower=='abril' or mes_seleccionado=='junio' or mes_seleccionado=='septimebre' or mes_seleccionado=='noviembre':
        for dia in range(1,31):
            print(dia)
    else:
        for dia in dias:
            print(dia)
    dia_seleccionado=input('=> ')



    print('***seleccione la hora del evento***')
    for hora in horas:
        print(hora)
    hora_seleccionada=input('=> ')

    evento=[mes_seleccionado,dia_seleccionado,hora_seleccionada]
    return evento

def crear_evento(nombre_evento,fecha):
    evento={nombre_evento:fecha}
    return evento


def verificar_disponibilidad(nombre_evento,fecha,ocupado,meses,dias,horas):
    for evento in ocupado:
        if fecha[0] and fecha[1] and fecha[2] in evento:
            print(f'\n Ya hay un evento agendado para esta fecha: {evento[0]}  {evento[1]}  {evento[2]}')
            print('\npor favor ingrese una nueva fecha\n')
            fecha=tomar_fecha(meses,dias,horas)
            break
        return True, ocupado
    print(f'Evento agendado con exito: {nombre_evento} :  {fecha[0]}  {fecha[1]}  {fecha[2]}')
    fecha.append(nombre_evento)
    ocupado.append(fecha)
    return False, ocupado


    


def mostrar_eventos(ocupado): 
    print('\nNOMBRE: MES - DIA - HORA')
    for evento in ocupado:
        print(f'{evento[-1]}: {evento[0]} - {evento[1]} - {evento[2]}')
    



def main():
    welcome()
    ocupado=[]
    meses=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
    dias=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
    horas=['12:00 AM','1:00 AM','2:00 AM','3:00 AM','4:00 AM','5:00 AM','6:00 AM','7:00 AM','8:00 AM','9:00 AM','10:00 AM','11:00 AM','12:00 PM','1:00 PM','2:00 PM','3:00 PM','4:00 PM','5:00 PM','6:00 PM','7:00 PM','8:00 PM','9:00 PM','10:00 PM','11:00 PM']
    while True:
        accion=get_option()
        if accion=='1':
            nombre_evento=tomar_nombre()
            fecha=tomar_fecha(meses,dias,horas)
            evento=crear_evento(nombre_evento,fecha)
            #ocupado.append(evento)
            unavailable=True
            while unavailable:
                unavailable, ocupado=verificar_disponibilidad(nombre_evento,fecha,ocupado,meses,dias,horas)

            
        elif accion=='2':
            if ocupado==[]:
                print('Por los momento no hay ningun evento agendado')
            else:
                mostrar_eventos(ocupado)
            

            
            pass
        else:
            break




main()
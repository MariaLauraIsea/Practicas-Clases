#while quit false se siguen mostrando las opciones de operacion
quit=False

infraction={
    1:{"name":"Choque", "cost":50},
    2:{"name":"Semáforo", "cost":30},
    3:{"name":"Falta de documentos", "cost":100},
}

officers={
    1:{"name":"Luis", "lastName":"Bello","ci":13452224},
    2:{"name":"Jose", "lastName":"Quevedo","ci":44235611},
    3:{"name":"Antonio", "lastName":"Guerra","ci":12345678},
}

db={}

aux=1

while quit==False:
    option=input('\nPor favor seleccione una operacion a realizar:\n1-Ingresar infractor\n2-Eliminar infractor\n3-Mostrar multas registradas\n4-Salir\n=> ')
    while not option.isnumeric or 0>int(option)>4:
        option=input('\nSeleccion invalida. Por favor seleccione una operacion a realizar:\n1-Ingresar infractor\n2-Eliminar infractor\n3-Mostrar multas registradas\n4-Salir\n=> ')
    if int(option)==1:
        multa={}
        n=1
        while n==1:
            name=input('ingrese su nombre: ')
            multa['nombre']=name
            lastname=input('ingrese su apellido: ')
            multa['apellido']=lastname
            cedula=input('ingrese su numero de cedula: ')
            multa['cedula']=cedula
            infraccion=input('seleccione un tipo de infraccion:\n1-choque\n2-semaforo\n3-falta de documentos\n=> ')
            while not infraccion.isnumeric() or  1>int(infraccion)>3:
                infraccion=input('seleccion no existe.  seleccione un tipo de infraccion:\n1-choque\n2-semaforo\n3-falta de documentos\n=> ')
            
            for type,inf in infraction.items():
                infraction_selcted=infraction[int(infraccion)]
                multa['infraccion']=infraction_selcted
            
            oficial=input('seleccione el fiscal que ha registrado la multa de infraccion:\n1-Luis Bello\n2-Andres Quevedo\n3-Antonio  Guerra\n=> ')
            while not oficial.isnumeric() or  1>int(oficial)>3:
                oficial=input('seleccion invalida. seleccione el fiscal que ha registrado la multa de infraccion:\n1-Luis Bello\n2-Andres Quevedo\n3-Antonio  Guerra\n=> ')
            for type,inf in officers.items():
                officer_selcted=officers[int(oficial)]
                multa['fiscal']=officer_selcted
            
            db[f'{aux}']=multa
            n+=1
        print(db)
        aux+=1

    elif int(option)==2:
        print(db)
        multa_eliminar=input('indique el numero de la multa que desea eliminar de la base de datos: ')
        while not multa_eliminar.isnumeric():
            multa_eliminar=input('ingreso invalido. indique el numero de la multa que desea eliminar de la base de datos: ')

        db.pop(multa_eliminar)
        print('la multa ha sido eliminada con exito')
        print(db)
         
    elif int(option)==3:
        for registrado,info in db.items():
            print(f'\nMULTA {registrado}')
            for dato,score in multa.items():
                print(dato,':', score)


    else:
        quit=True
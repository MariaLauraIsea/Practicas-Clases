def es_par(price):
    if price%2==0:
        return True
    else:
        return False#preguntar forma mas facil de hacer nros primos
        
            


def es_primo(rif):
    nro=int(rif[-1])
    aux=nro-1
    while aux>1:
        if nro%aux==0:
            return False
        aux+=1
    return True
    


def register(db):
    while True:
        try:
            rif=input('ingrese el rif: ')
            name=input('ingrese la razon social: ')
            product=int(input('ingrese el producto 0:Quimico,  1:Farmaceutico,  2:Biologico  => '))
            if product!=0 and product!=1 and product!=2:
                raise Exception
            payment_method=int(input('ingrese el metodo de pago 0:Contado,  1:Credito  =>  '))
            if payment_method!=0 and payment_method!=1:
                raise Exception
            break
        except:
            print('Error!')

    if product==0:
        price=10
        tax=price*0.16
        productname='Quimico'
    elif product==1:
        price=25
        tax=0
        productname='Farmaceutico'
    else:
        price=40
        tax=price*0.16
        productname='Biologico'

    discount=0
    extra_amount=0
    if payment_method==1:
        formapago='Credito'
        extra_amount=price*.10
    else:
        formapago='Contado'
        discount=price*.03

    total=price+tax-discount+extra_amount-discount
    total=round(total,2)

    if es_par(price):
        total=total-(total*.02)

    if es_primo(rif):
        total=total-(total*0.05)

    compra={'rif':rif,'razon social':name,'producto':productname,'forma de pago':formapago,'descuento':discount,'tax':tax,'TOTAL A PAGAR':total}
    db.append(compra)
    return db,compra

    
def factura(compra):
    print('****DATOS DE COMPRA****')
    for key,value in compra.items():
        print(f'{key}: {value}')


def total_clients(db):
    quimicos=filter(lambda person:person['product']==0,db)#not gonna work person lo pusiste como dic


def main():
    db=[{'rif':'j-484848','name':'Avila Tek','product':0,'payment_method':0,'discount':5,'tax':2,'total_amount':10}]
    while True:
        option=input('''
        Saman International
        1. Registro
        2. Estadisticas
        3. Salir
        => ''')
        if option=='1':
            db,compra=register(db)
            factura(compra)
            total_clients(db)

        elif option=='2':
            pass
        else:
            break


main()
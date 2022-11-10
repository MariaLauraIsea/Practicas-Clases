def get_datos():
    while True:
        try:
            sub_total=int(input('Ingrese el monto total de la factura sin IVA: $ '))
            break
        except:
            print('Ingreso invalido para continuar')

    opcion=input('Desea especificar el porcentaje de IVA a aplicar? Si S o No N: ')
    if opcion=='S':

        while True:
            try:
                IVA=int(input('Ingrese el porcentaje de iva a aplicar: % '))
                IVA=IVA/100
                break
            except:
                print('Ingreso invalido para continuar')
    else:
        IVA=21/100
    return sub_total,IVA


def get_total(sub_total,IVA):
    total=(sub_total*IVA)+sub_total
    print(f'El total de su factura con el IVA aplicado es de {total}$')


def main():
    sub_total, IVA=get_datos()
    get_total(sub_total,IVA)


main()
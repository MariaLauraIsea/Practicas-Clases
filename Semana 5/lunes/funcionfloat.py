def parse_float (numero,separador):
    try:
        res= float(numero)
    except:
        res=float(numero.replace(separador,'.'))
    return res


def main():
    numero=input('ingrese un numero flotante: ')
    separador= input('ingrese el separador del numero: ')
    res= parse_float(numero,separador)
    print(f'el numero flotante es {res}')

main()
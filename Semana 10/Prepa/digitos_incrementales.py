def es_incremental(n,i=0):
    if len(n)==i+2:
        return 'es de digitos incrementales'

    elif int(n[i])>int(n[i+1]):
        return 'no es de digitos incrementales' 

    return es_incremental(n,i+1) #FOTO




def main():
    n=input('ingrese u numero antural de dos o mas digitos: ')
    while not n.isnumeric() or len(n)<2:
        n=input('ingreso invalido\ningrese u numero antural de dos o mas digitos: ')

    resultado=es_incremental(n)
    print(resultado)



main()
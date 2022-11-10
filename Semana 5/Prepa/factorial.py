def factorial(numero):
    f=1
    for x in range(2,numero+1):
        f*=x
        
    return f
    

def main():

    while True:
        try:
            numero=int(input('ingrese un numero natural: '))
            if numero==0:
                raise Exception
            break
        except:
            print('ingreso invalido')
        
    f=factorial(numero)
    print(f'el factorial de {numero} es {f}')




main()
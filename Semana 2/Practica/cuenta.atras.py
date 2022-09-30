n=input('ingres un numero entero positivo: ')

while not n.isnumeric() or int(n)<=0:
    n=input('ingreso invalido. ingrese un numero entero positivo:')
    


for i in range(int(n),-1,-1):
    print(i, end=', ')

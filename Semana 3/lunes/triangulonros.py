number= input('ingrese un numero entero positivo: ')

while not number.isnumeric() or int(number)<=0:
    number=input('ingreso invalido. ingrese un numero entero positivo')

number=int(number)


for n in range(1,number+1,2):
    aux= n
    while aux>=1:
        if aux == 1:
            print(n)
        else:
            print(aux,end=' ')
        aux-=2
    
for n in range(1,number+1,2):
    for j in range(n,0,-2):
        print(j, end=' ')
    print('')
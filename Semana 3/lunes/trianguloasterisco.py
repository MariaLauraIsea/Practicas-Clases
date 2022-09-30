altura= input('ingrese un numero entero positivo: ')

while not altura.isnumeric() or int(altura)<=0:
    altura=input('ingreso invalido. ingrese un numero entero positivo')

altura=int(altura)

for a in range(1,altura+1):
    print('*'*a)
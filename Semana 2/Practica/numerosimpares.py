numero= input('ingrese un numero entero positivo:')

while not numero.isnumeric() or int(numero)<=0:
    numero=input('ingreso invalido. ingrese un numero entero positivo:')


for i in range(1,int(numero)+1,2):
    print(i, end= ', ')





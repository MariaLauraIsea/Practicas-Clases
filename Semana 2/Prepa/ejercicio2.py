numero= input('ingrese un numero entero positivo: ')

while not numero.isnumeric() or int(numero)==0 :
    numero=input('ingreso invalido. ingrese un numero entero positivo: ')

while len(numero) > 1:
    aux=0
    print('aux inicial', aux)
    for d in numero:
        aux+= int(d)
        print('sumando:',aux)
    numero=str(aux)
    
print('la suma de los digitos del numero es:',numero)
    
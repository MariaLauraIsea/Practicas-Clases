from operator import truediv


number=input('ingrese un numero ')

while not number.isnumeric():
    number=input('ingreso invalido\ningrese un numero ')

comprobador=True
first_digit=number[0]


for digit in number:
    if digit != first_digit:
        comprobador=False
    
if comprobador:  #== True
    print(f'el numero {number} es un numero repunit')
else:
    print(f"el numero {number} no es un numero repunit")



sum_digits=0

for digit in number:
    sum_digits += int(digit)

raiz= (int(sum_digits)**(1/2))
raizentera= int(raiz)

if ((raiz/raizentera)==1):
    print(f'la suma de los digitos del numero {number} es un numero cuadrado')
else:
    print(f'el numero {sum_digits} no es un numero cuadrado')
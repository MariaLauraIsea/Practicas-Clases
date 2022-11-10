number=int(input('por favor ingrese un numero: '))

comprobador=False
natural=0

while natural <=9:
    if natural*(natural+1)==number:
        comprobador=True
        break
    natural +=1
    
if comprobador==True:
    print(f'el numero {number} es oblongo')
else:
    print(f'el numero {number} no es oblongo')



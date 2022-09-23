tope=input('ingrese el tope de la sucesion:')

while not tope.isnumeric() or int(tope)==0:
    tope=input('ingreso invalido. ingrese el tope de la sucesion:')

x=0
y=1
z=1
sucesion=[str(x),str(y)]

while int(tope)>z:
    sucesion.append(str(z))
    x=y
    y=z
    z= x + y #f(n)=f(n-2)+f(n-1)
    print(x,y,z)
    print(sucesion)

print(', '.join(sucesion))

from defobjeto import Bicicleta
from ClaseHija import BicicletaElectrica,BicicletaKids



def main():
    bici1=Bicicleta('rojo','cuero','bajo')
    bici1.identidad()
    print(bici1.asiento) #para acceder a la info de un valor en especifico
    
    #guardando los atributos como una variable y accediendo mediante la variable
    
    atributos_bici1=bici1.extraer()
    for atributos,value in atributos_bici1.items():
        print(f'{atributos}: {value}')

    color_bici1=bici1.identidad_color()
    print(color_bici1)
    bici_kid=BicicletaElectrica('azul','cuero','alto','50 km/h')
    color2=input('ingrese el color de la bicicleta: ')
    asiento2=input('ingrese el material del asiento: ')
    manubrio2=input('ingrese el tipo de manubrio: ')
    bici2=Bicicleta(color2,asiento2,manubrio2)
    bici2.identidad()
     


main()
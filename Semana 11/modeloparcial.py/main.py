from BebidaAlcoholica import Alcoholica
from NoAlcoholica import NoAlcoholica
from Cliente import Cliente
from Factura import Factura

def register_drink(bebidas):
    type=int(input('Que tipo de bebida desea registrar?\n1 - Alcoholica\n2 - No Alcoholica\n=> '))
    if type==1:
        name=input('Nombre de la bebida: ')
        price=int(input('Precio de la bebida: $'))
        grado=int(input('Grado alcoholico: °'))
        bebida=Alcoholica(name,price,grado)
        bebidas.append(bebida)

    else:
        name=input('Nombre de la bebida: ')
        price=int(input('Precio de la bebida: $'))
        temp=int(input('Temperatura de consumo: °'))
        bebida=NoAlcoholica(name,price,temp)
        bebidas.append(bebida)
    return bebidas
    
def register_client(clients):
    name=input('Ingrese su nombre: ')
    cedula=input('Ingrese su cedula: ')
    age=int(input('Ingrese su edad: '))
    client=Cliente(name,cedula,age,None)
    clients.append(client)
    return client,clients

def get_products():
    pass

def main():
    bebidas=[NoAlcoholica('Coca-Cola',2,12),Alcoholica('Cerveza',1.5,6),NoAlcoholica('Red Bull',3,10)]
    clients=[]
    while True:
        option=int(input('Seleccione una opcion para continuar:\n1 - Registrar bebida\n2 - Nueva compra\n3 - Salir\n=> '))
        if option==1:
            bebidas=register_drink(bebidas)

        elif option==2:
            registered=input('Usted se encuentra registrado en el sistema?\nS - SI\nN - NO\n=> ').upper()
            if registered== 'S':
                for bebida in bebidas:
                    bebida.show()
            else:
                client,clients=register_client(clients)
                for bebida in bebidas:
                    if client.edad<18:
                        if bebida.type =='no alcoholica':
                            bebida.show()
                    else:
                        bebida.show()
                get_products()

        #VER FOTO Y TERMINAR MODELO PARCIAAAAAAAAAAL    
        
        else:
            break

main()
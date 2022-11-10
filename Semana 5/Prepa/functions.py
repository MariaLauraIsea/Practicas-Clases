import random

def generar_tickets():

    tickets=[]
    while True:
        try:
            amount=int(input('ingrese la cantidad de tickets a generar: '))
            if amount==0:
                raise Exception
            break
        except:
            print('ingreso invalido')
            

    while len(tickets)<amount:
        t=random.randint(10000000,99999999)
        if not t in tickets:
            tickets.append(t)

    return tickets
    



def elegir_ganador(t):
    return random.choice(t)
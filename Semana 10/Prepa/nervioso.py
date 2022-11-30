import random
def nervioso(cartas,aleatoria,actual=0):
    print('\ncarta aleatoria:',cartas[aleatoria])
    print('carta actual:',cartas[actual])
    if aleatoria==actual:
        return 'fin de la ronda'

    return nervioso(cartas,random.randint(0,12),0 if actual==12 else actual+1)
    

def main():
    cartas=['A' if n==1 else'J' if n==11 else 'Q' if n==12 else 'K' if n==1 else n for n in range(1,14)] #wtf

    fin=nervioso(cartas,random.randint(0,12))
    print(fin)


main()
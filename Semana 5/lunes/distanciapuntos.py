

def main():
    P1=(5,10)
    P2=(3,-2)

    distancia= lambda P1,P2: (((P2[0]-P1[0])**2 + (P2[1]-P1[1])**2)**0.5)
    print(distancia(P1,P2))



main()
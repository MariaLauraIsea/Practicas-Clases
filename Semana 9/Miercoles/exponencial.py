def exponencial(b,e):
    if e==0:
        return 1

    return b*exponencial(b,e-1)


def main():
    b=int(input('ingrese la base: '))
    e=int(input('ingrese el exponente: '))
    total= exponencial(b,e)
    print(total)


main()
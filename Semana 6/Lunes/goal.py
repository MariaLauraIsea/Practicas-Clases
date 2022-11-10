def parser(codigo):
    codigo=codigo.replace('()','o')
    codigo=codigo.replace('(al)','al')
    return codigo


def main():
    codigo=input('enter the goal parser alphabet: ')
    traduccion=parser(codigo)
    print(traduccion)


main()
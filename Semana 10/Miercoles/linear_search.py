def main():
    lista=[6,5,3,1,8,7,2,4]
    number=int(input('please enter a number to search on the list: '))
    if lineal_search(lista,number):
        print('the number',number,'was found on the list')

    else:
        print('the number',number,'was not found on the list')


def lineal_search(lista,number):
    for n in lista:
        if n==number:
            return number


main()
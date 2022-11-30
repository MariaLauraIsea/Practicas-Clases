#PREFERIBLE USAR ESTA

def main():
    lista=[6,5,3,1,8,7,2,4]
    number=int(input('please enter a number to search on the list: '))
    lista2=selection(lista)
    if binary_search(lista2,number)!=-1:
        print('the number',number,'was found on the list')

    else:
        print('the number',number,'was not found on the list')


def selection(lista):
    for i in range(len(lista)):
        menor=i     #para que no se pierda el valor
        for j in range(i+1,len(lista)):
            if lista[j]<lista[menor]:
                menor=j
        temp=lista[i]
        lista[i]=lista[menor]
        lista[menor]= temp
    return lista

def binary_search(lista,number):
    start=0
    final=len(lista)-1
    middle= (start+final)//2
    if len(lista)==1:
        if lista[0]==number:
            return number
        else:
            return -1   #simboliza: no lo consegui  puede equivaler a un false

    if number>lista[middle]:
        return binary_search(lista[middle:final],number)
    elif number<lista[middle]:
        return binary_search(lista[start:middle],number)
    else:
        return number

main() #tqm lauri
#REVISAR GITHUB PORQUE NO CORRE EL PROGRAMA


def buscar_letra(letras,letra,index=0):
    if letra==letras[index]:         #para todas las letras
        return letra
    else:
        if index==len(letras)-1:     #para la ultima letra
            if letra==letras[index]:
                return letra
            else:
                return None
    

    return buscar_letra(letras,letra,index+1)



def main():
    letras=['a','b','c','d','e','f']
    letra=input('indique la letra que quiere buscar en la lista: ').lower
    resultado=buscar_letra(letras,letra)
    print('la letra fue encontrada',resultado)


main()
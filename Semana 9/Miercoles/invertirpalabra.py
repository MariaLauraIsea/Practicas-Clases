#ENTENDER COMO FUNCIONA

def invert_word(palabra,index):
    if index==0:
        return palabra[index]

    return palabra[index]+invert_word(palabra,index-1)

def main():
    palabra=input('ingrese la palabra que quiere invertir: ')
    invertida=invert_word(palabra,len(palabra)-1)
    print(invertida)


main()
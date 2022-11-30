def factorial(number):
    if number==0 or number==1:
        return 1
    else:
        return number*factorial(number-1)
    

def main():
    number=int(input('ingrese un numero para calcular su factorial: '))
    f=factorial(number)
    print('el factorial de',number,'es',f)

main()
def fibonacci(max,num1,num2):
    if num1>max:
        return num1
    else:
        print(num1,end=' ')
        return fibonacci(max,num1=num2,num2=num1+num2)

def es_fibonacci(number,num1,num2):
    if num1==number:
        return True
    if num1>number:
        return False
    else:
        return es_fibonacci(number,num1=num2,num2=num1+num2)
def main():

    max=int(input('ingrese el tope de la secuencia: '))
    fibonacci(max,num1=0,num2=1)
    number=int(input('\ningrese un numbero para saber si es fibonacci: '))
    result=es_fibonacci(number,num1=0,num2=1)
    if result:
        print('el numero',number,'si es fibonacci')
    else:
        print('el numero',number,'no es fibonacci')

main()
def get_number():
    while True:
        try:
            number=int(input('please enter a number: '))
            return number
            break
        except:
            print('please enter a valid number')
        

def get_fibonacci(number):
    fibonacci=['0']
    cont=1
    if number==0:
        return fibonacci
    elif number==1:
        fibonacci.append(str(1))
        return fibonacci
    else:
        fibonacci.append(str(1))
        while cont<number:
            for digit in range(2,number+1):
                nro_fibonacci=(digit-1)+(digit-2)
                fibonacci.append(str(nro_fibonacci))
                print(cont)
                cont+=1
        return fibonacci


def main():
    number=get_number()
    fibonacci=get_fibonacci(number)
    print(f'if the number is {number}')
    print('the fibonacci sequence is:')

    print(', '.join(fibonacci))


main()
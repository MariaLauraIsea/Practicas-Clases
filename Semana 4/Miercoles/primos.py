def isprime(number):
    if (number<=0):
        return False
    aux=2
    prime= True

    while aux <number:
        if (number%aux ==0):
            prime=False
            break
        aux+=1
    return prime
        
             

def main():
    print(isprime(2))
    print(isprime(6))

main()
number=input('Please enter a natural number: ')

while not number.isnumeric() or int(number)<0:
    number=input('invalid number\nplease enter a natural number: ')

isfermat=True
n=0
fermat=0

while int(number)>fermat:
    fermat=((2**(2**n))+1)
    print(fermat)
    print(isfermat)
    if fermat!=int(number):
        isfermat=False
        
    n+=1

print(isfermat)
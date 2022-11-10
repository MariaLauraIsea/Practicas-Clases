number=input('Please enter a natural number: ')

while not number.isnumeric() or int(number)<0:
    number=input('invalid number\nplease enter a natural number: ')


n=0
aux=2
fermat=3

while fermat<int(number):
    fermat=((2**(2**n))+1)
    print(fermat)
    n+=1

print(fermat%aux==0, 'ok')
isfermatprime= True

while aux<int(fermat):
    if (fermat%aux ==0):
        isfermatprime=False
        break
    aux+=1

print(isfermatprime)
print(fermat)

if isfermatprime==True:
    print(f'the number {number} is fermat prime')
else:
    print(f'the number {number} is not fermat prime')
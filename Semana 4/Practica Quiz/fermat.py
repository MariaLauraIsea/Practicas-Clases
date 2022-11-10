number=input('please enter a natural number: ')

while not number.isnumeric() or int(number)<0:
    number=input('invalid entree. please enter a natural number: ')

isfermatprime=True
fermat=((2**(2**(int(number)))+1))

for divisores in range(2,fermat):
    if (fermat%divisores==0):
        isfermatprime=False
    break

print(fermat)

if isfermatprime:
    print('the number calculated is fermat prime')

else:
    print('the number calculated is not fermat prime')

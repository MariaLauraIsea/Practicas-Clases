number=input('please enter a number: ')

while not number.isnumeric():
    number=input('invalid entree. please enter a number: ')

for digit in range(len(number)-1,-1,-1)
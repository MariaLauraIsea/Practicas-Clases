from turtle import back


number=input('please enter a number: ')

while not number.isnumeric():
    number=input('invalid entree. please enter a number: ')

palindromo=True

for digit in range(0,int(number)+1):
    for backward_digit in range(int(number)+1,0):
        print(backward_digit)
        if int(digit)!=(backward_digit):
            palindromo=False

#for digit in range(len(number)):
 #   for bacward_digit in range((int(number)+1),0):
 #       if int(digit)!=int(bacward_digit):
  #          palindromo=False


if palindromo:
    print(f'the number {number} is palindromic')
else:
    print(f'the number {number} is not palindromic number')
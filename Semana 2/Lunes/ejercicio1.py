number1 = input("enter a number ")
number2 = input("enter another number ")
is_valid = True

if number1 .isnumeric():
    number1= float(number1)
else:
    is_valid= False

if number2 .isnumeric():
    number2= float(number2)
else:
    is_valid= False

if number2 == 0:
    print("error")
else:
    print(number1/number2)
    

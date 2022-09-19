number= input("please enter a number ")
is_valid = True

if number .isnumeric():
    number = float(number)

if number %2 == 0:
    print(f"the number {number} is even")
else:
    print(f"the number {number} is odd")
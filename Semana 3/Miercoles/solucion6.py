from ast import Break


informacion={}

while True:
    key_name=input('what data do you want to save?: eg. name, age:')
    value= input('please enter the data value: ')
    informacion[key_name]=value

    for key, value in informacion.items():
        print(f"your {key} is {value}")

    if input('do you want to exit?:\n Y-Yes \n N-No \n => ') =='Y':
        break


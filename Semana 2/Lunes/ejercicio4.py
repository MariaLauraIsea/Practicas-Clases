option= int(input("please enter a valid option: \n1 - vegetarian \n2 - non vegetarian \n =>"))
if option == 1:
    ingrediente= int(input("please enter a valid option: \n1 - pimiento \n2 - tofu \n =>"))
    if ingrediente == 1:
        ingrediente= 'pimiento'
    else:
        ingrediente= 'tofu'
    print(f'the pizza is vegetarian and has these ingredients tomato, mozarella and {ingrediente}')
      
elif option == 2:
    ingrediente= int(input("please enter a valid option: \n1 - peperioni \n2 - jamon \n3 - salmon \n =>"))
    if ingrediente == 1:
        ingrediente= 'peperoni'
    elif ingrediente == 2:
        ingrediente= 'jamon'  
    else:
        ingrediente= 'salmon'
    print(f'the pizza is non vegetarian and has these ingredients tomato, mozarella and {ingrediente}')
else:
    print("invalid option")
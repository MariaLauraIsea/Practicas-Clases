diccionario={}

palabra=input('escriba diccionario en el siguiente formato: <palabra>:<traducción> separado por una coma: ')
traduccion=palabra.split(',')

for translation in traduccion:
    list_of_values= translation.split(':')
    translate_key=list_of_values[0]
    translate_value=list_of_values[1]
    diccionario[translate_key]=translate_value
print(diccionario)
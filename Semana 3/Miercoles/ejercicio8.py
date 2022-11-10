diccionario={}

palabra=input('escriba diccionario en el siguiente formato: <palabra>:<traducción> separado por una coma: ')
traduccion=palabra.split(',')

for translation in traduccion:
    list_of_values= translation.split(':')
    translate_key=list_of_values[0]
    translate_value=list_of_values[1]
    diccionario[translate_key]=translate_value

phrase_input= input('por favor ingrese una frase para traducir: ')
word_list= phrase_input.split(' ')
result_words=''

for word in word_list:
    result_words+= diccionario.get(word,word)
    result_words+=''

print(result_words)


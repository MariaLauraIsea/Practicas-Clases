elementos={"hidrogeno": 1, "helio": 2, "carbon": 6}
elementos["litio"]=3
print(elementos)

print(elementos.get('oxigeno',"no existe"))

for key, value in elementos.items():
    print('el elemento {} tiene un numero atomico de {}'.format(key,value))

print(elementos.get('oxi') is None)

#para quitar keys es .pop()
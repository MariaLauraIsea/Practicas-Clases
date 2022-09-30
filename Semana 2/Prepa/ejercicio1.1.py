lista='bienvenidos a la prepa de algoritmos a'
count=0

for i in lista:
    if i=='a'and len(lista) > count+1:
        if lista[count+1]=='l':
            print(f'hay un al en el punto {count} y {count+1}')
    count+=1
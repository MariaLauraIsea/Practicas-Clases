lista = [ ["DOWN","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"],["DOWN","DOWN","LEFT","LEFT","LEFT","LEFT","LEFT"], ["DOWN","WALL","RIGHT","DOWN","DOWN","LEFT","LEFT"],
["RIGHT","RIGHT","UP","DOWN","DOWN","RIGHT","DOWN"], ["WALL","DOWN","LEFT","LEFT","RIGHT","UP","DOWN"], ["UP","RIGHT","RIGHT","RIGHT","RIGHT","RIGHT","DOWN"], ["UP","LEFT","LEFT","LEFT","LEFT","LEFT","EXIT"]
]

x=0
y=0

def recorrer(lista,x,y):
    if lista[x][y] == "DOWN":
        print('\nyou moved down!')
        return recorrer(lista,x+1,y)
    elif lista[x][y] == "UP":
        print('\nyou moved up!')
        return recorrer(lista,x-1,y)
    elif lista[x][y] == 'RIGHT':
        print('\nyou moved right!')
        return recorrer(lista,x,y+1)
    elif lista[x][y] == 'LEFT':
        print('\nyou moved left!')
        return recorrer(lista,x,y-1)
    elif lista[x][y] == 'WALL':
        print('\nyou hit a wall!')
        return recorrer(lista,x,y)
    else:
        print('\nyou have made it out of the labyrinth!!!!!')


recorrer(lista,x,y)
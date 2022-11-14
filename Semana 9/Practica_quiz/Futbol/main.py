from Equipo import Equipo
from Tecnico import Tecnico
from Jugador import Jugador

def register(personas):
    info_personas=[{'nombre':'javier','ci':'25664897','tiempo':5,'sueldo':5000,'juego estrellas':False,'persona':'jugador','posicion':'defensa'},{'nombre':'marco','ci':'21164897','tiempo':2,'sueldo':8000,'juego estrellas':True,'persona':'jugador','posicion':'arquero'},
    {'nombre':'daniel','ci':'14664897','tiempo':6,'sueldo':10000,'persona':'tecnico','tipo':'entrenador'},
    {'nombre':'ignacio','ci':'23444897','tiempo':3,'sueldo':7000,'juego estrellas':True,'persona':'jugador','posicion':'delantero'},
    {'nombre':'martin','ci':'246227897','tiempo':4,'sueldo':8000,'juego estrellas':True,'persona':'jugador','posicion':'delantero'}
    ]
    personas=[]

    for p in  info_personas:
        if p['persona']=='jugador':
            persona=Jugador(p['nombre'],p['ci'],p['tiempo'],p['sueldo'],p['posicion'],p['juego estrellas'])
        else:
            persona=Tecnico(p['nombre'],p['ci'],p['tiempo'],p['sueldo'],p['tipo'])

        personas.append(persona)


    return personas


def main():
    personas=[]
    personas=register(personas)
    equipo=[]
    for p in personas:
        if type(p)==Jugador:
            if p.juego_estrella==True:
                equipo.append(p)
    estrellas=Equipo(equipo)
    estrellas.recorrer(personas)



main()
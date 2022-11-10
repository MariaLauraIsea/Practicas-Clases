from Redactor import Redactor
from Jefes import Jefe
from Secciones import Seccion


def get_redactores_entretenimiento():
    return[
        Redactor('leonardo',254488976)
    ]



def get_redactores_farandula():
    return[
        Redactor('andres',254488976)    
    ]


def get_redactores_deportes():
    return[  
        Redactor('guillermo',254488976)
    ]


def process_articles(seccion):
    print('\ninicio de labores en la seccion',seccion.nombre)
    print('el jefe al mando es: ',seccion.jefe.name)
    articles=[]
    for escritor in seccion.jefe.redactores_supervisados:
        print('el escritor en labor es:',escritor.name)
        articulo=escritor.escribir_articulo()
        articulo.redactor=escritor.name

        if seccion.jefe.decidir(articulo):
            articles.append(articulo)





def main():
    jefe_redactor_entretenimiento=Jefe('Jose Quevedo',25225,get_redactores_entretenimiento())
    jefe_redactor_farandula=Jefe('Juan Landaeta',25225,get_redactores_farandula())
    jefe_redactor_deportes=Jefe('Antonio Guerra',25225,get_redactores_deportes())

    seccion_entretenimiento=Seccion(jefe_redactor_entretenimiento,'Entretenimiento')
    seccion_farandula=Seccion(jefe_redactor_farandula,'Farandula')
    seccion_deportes=Seccion(jefe_redactor_deportes,'Deportes')

    process_articles(seccion_entretenimiento)
    process_articles(seccion_farandula)
    process_articles(seccion_deportes)

   



#github prof



main()
from functions import generar_tickets, elegir_ganador



def main():
    tickets=generar_tickets()
    ganador=elegir_ganador(tickets)
    print(f'el ganador es el ticket {ganador}')





main()
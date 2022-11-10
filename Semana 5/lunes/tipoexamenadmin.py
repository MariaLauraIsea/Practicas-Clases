def print_welcome():
    print('*****Welcome*******')

def get_option(studies):
    for key,value in studies.items():
        for key_interno, value_interno in value.items():
            print(f'{key} - {value_interno}', end='')
        print('')
    return input('please enter an option:  ')

def get_client_data(study):
    client= {
        'id':input('please enter the client id: '),
        'age':input('please enter the client age: '),
        'gender':input('please enter the client gender M or F: '),
        'study':study
    }
    return client


def get_net_amount(client,discount,studies):
    return studies.get(client.get('study')).get('price')-discount



def print_invoice(client,studies,total):
    print('***** RECEIPT *****')
    print('id card: ',client.get('id'))
    print('age: ',client.get('age'))
    print('gender: ',client.get('gender'))
    print('study: ',studies.get(client.get('study')).get('description'))
    print('net amount: ',studies.get(client.get('study')).get('price')) #arreglar

def get_discounts(client,studies,client_number):
    discount=0
    if client.get('gender')== 'F' and int(client.get('age')) > 55:
        discount += studies.get(client.get('study')).get('price') * 0.25
    elif client.get('gender')== 'M' and int(client.get('age')) > 65:
        discount += studies.get(client.get('study')).get('price') * 0.25

    if client_number % 2 !=0:
        discount+= studies.get(client.get('study')).get('price')*0.02 
    return discount

def print_final_day(clients):
    pass

def main():
    studies_dic={
        'U':{
            'description':'ultrasonido',
            'price':8900
        },
        'T':{
            'description':'tomografia',
            'price':12640
        },
        'R':{
            'description':'radiografia',
            'price':15600
        }

    }
    
    clients=[]
    total_discounts=0
    total_net_amount=0
    total_net_U=0
    total_net_T=0
    total_net_R=0
    client_U=0
    client_T=0
    client_R=0

    print_welcome()
    while True:
        option=get_option(studies_dic)
        client=get_client_data(option)
        clients.append(client)
        discount=get_discounts(client,studies_dic,len(clients))
        total_discounts+=discount
        
        total=get_net_amount(client,discount,studies_dic)
        total_net_amount+=total
        print_invoice(client,studies_dic,total)



        if option=='U':
            client_U+=1
            total_net_U+=total_net_amount
        if option=='T':
            client_T+=1
            total_net_T+=total_net_amount
        if option=='R':
            client_R+=1
            total_net_R+=total_net_amount


        print('****END OF DAY*****')
        print('clients U',client_U)
        print('clients T: ',client_T)
        print('clients R: ',client_R)
        if  len(clients)==0:
            print('Average: 0')
        else:
            print('Average: ',total_net_amount/len(clients))

        if  client_U==0:
            print('Average: 0')
        else:
            print('Average: ',total_net_U/client_U)

        if input('do you want to continue  Y yes or N no?') == 'Y':
            break
    
    #print_final_day(clients) Si se quiere hacer con funciones
    


main()
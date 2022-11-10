from cmath import rect


def is_prime(rif):
    nro=int(rif[-1])
    aux=nro-1
    while aux>1:
        if nro%aux==0:
            return False
        aux-=1

    return True



def main():
    products={'F':{'descripcion':'Farmaceutico','precio':2500}, 'Q':{'descripcion':'Quimico','precio':100},'B':{'descripcion':'Biologico','precio':4000}}
    
    client_f=0
    client_q=0
    client_b=0
    discount_f=0
    discount_q=0
    discount_b=0
    max_purchase=0
    rif_max_purchase=0
    total_day=0

    print('Bienvenido al programa')
    while True:
        print('\nComplete los datos para registrar la compra\n')
        rif=input('ingrese su rif: ')
        product_code=input('ingrese el codigo del producto:\nF-Farmaceutico\nQ-Quimico\nB-Biologico\n=> ')
        payment=input('ingrese el tipo de pago:\nC-Contado\nR-Credito\n=> ')
        gross_amount=products.get(product_code).get('precio')
        
        discount=0
        recharge=0
        taxes=0

        #discounts
        if payment=='C':
            discount+=gross_amount*0.03
        elif payment=='R':
            recharge+=gross_amount*0.1


        if gross_amount%2==0:
            discount+=gross_amount*0.02

        if is_prime(rif):
            discount+=gross_amount*0.05


        #taxes

        if product_code!='F':
            taxes+=gross_amount*0.12

        #total
        
        total=gross_amount+recharge-discount+taxes

        print('***FACTURA***')
        print('RIF ',rif)
        print('Producto ',products.get(product_code).get('descripcion'))
        print('Forma de pago ', payment)
        print('Discount ',discount)
        print('Tax', taxes)
        print('Total ',total)

        # end of day data

        total_day+=total

        if product_code=='F':
            client_f+=1
            discount_f+=discount

        elif product_code=='Q':
            client_q+=1
            discount_q+=discount

        elif product_code=='B':
            client_b+=1
            discount_b+=discount


        if total>max_purchase:
            rif_max_purchase=rif
            max_purchase=total

        #areglar con menu
        print('*****END OF DAY*****')
        print('Client F: ',client_f)
        print('Client Q: ',client_q)
        print('Client B: ',client_b)
        print('Discounts F: ',discount_f)
        print('Discounts Q: ',discount_q)
        print('Discounts B: ',discount_b)


        

main()
def get_wealth(acounts):
    max=0
    for lista in acounts:
        if sum(lista)>max:
            max=sum(lista)
    
    return max



def main():
    acounts=[[1,2,3],[3,2,1],[3,6,9]]
    wealth=get_wealth(acounts)
    print('the max wealth is',wealth)



main()
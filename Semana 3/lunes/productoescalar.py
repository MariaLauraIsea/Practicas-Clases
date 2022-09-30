x=[1,2,3]
y=[-1,0,2]
acum_total=0

for index in range(len(x)):
    acum_total+= (x[index]*y[index])
    
print('result',acum_total)
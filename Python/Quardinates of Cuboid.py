#Take Quardinates of 3 Dimension Cubiod and return all possible quardinates lie inside cubiod and Quardinates sum is not equals to n


x = int(input())
y = int(input())
z = int(input())
n = int(input())
    
Lst=[]

    
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            
            if n!=i+j+j:
                Temp=[i,j,k]
                Lst.append(Temp)
            Temp=[]      
    
print(Lst)
    
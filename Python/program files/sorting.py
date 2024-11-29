n=int(input("Enter Range: "))
a=[None]*n
L=len(a)

for i in range(L):
    a[i]=int(input("Enter Number: "))

for i in range(L-1):
    for j in range(i+1,L):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]

print(a)    
    
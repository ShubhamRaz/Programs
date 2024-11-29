a=["Pankaj","Kumar","Shubham","Raj","helllo"]

for i in range(0,len(a)-1):
    if len(a[i]) > len(a[i+1]):
        a[i],a[i+1]=a[i+1],a[i]

print(a[-1])


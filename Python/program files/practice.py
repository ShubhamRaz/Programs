a=[1,2,3,4,5,6]
a1=[]
a2=[]
for i in range(0,len(a),2):
    a1.append(a[i])

for i in range(1,len(a),2):
    a2.append(a[i])

print(a1)
print(a2)

dict1=dict(zip(a1,a2))

print(dict1)

cube=lambda l:l*l*l

a3=list(map(cube,a))

print(a3)

def chang(a):
    return a>4


a4=list(filter(chang,a))

print(a4)
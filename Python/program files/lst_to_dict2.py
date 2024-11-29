x=int(input("Enter Range: "))

name=[None]*x
title=[None]*x

for i in range(x):
    name[i]=input("Enter Name: ")
    title[i]=input("Enter Title: ")

result=dict(zip(name,title))

print(result)

for i in result.keys():
    print(i) 


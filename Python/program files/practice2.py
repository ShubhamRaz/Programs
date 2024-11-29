


Dict1={
    1:"A",
    2:"B",
    3:"C",
    4:"D"
}



Lst=list(Dict1.keys())
print(Lst)

Lst2=list(Dict1.values())
print(Lst2)


a=input("Enter: ")

for i in a:
    flag=Lst2.index(i)
    print(Lst[flag],end="")

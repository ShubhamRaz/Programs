lst=["Pankaj",1,2,3,2,1,"Shubham","Pankaj"]
lst2=[1,2,3]
print(lst)

lst.pop(1)

print(lst)

lst.remove(2)

print(lst)
lst.append(1)
print(lst)
print(lst.count(1))
lst.extend(lst2)
print(lst)
lst.insert(1,"Hello")
print(lst)
print(lst.index(1))

print(lst[-1:-5:-1 ])
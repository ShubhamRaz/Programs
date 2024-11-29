# Line=input("Enter a line: ")
# upper=0
# lower=0
# digit=0
# symbal=0

# for i in Line:
#     if i.isupper():
#         upper+=1

#     elif i.islower():
#         lower+=1
#     elif i.isdigit():
#         digit+=1

#     elif i.isalpha():
#         symbal+=1

# print("Uppercase: ",upper)
# print("Lowercase: ",lower)
# print("Digits:",digit)
# print("Symbals: ",symbal)
# print("Total alphabets: ",upper+lower)



#vowels

# line=input("Enter Line: ")

# for i in line:
#     if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
#         print(i,end="")


#question

# num=int(input("Enter Number of Students Participated: "))
# dict1={}

# for i in range(1,num+1):
#     key=str(input(f"{i} Enter Name: "))
#     values=int(input("Enter their wins: "))
#     dict1[key]=values

# print(dict1)


# num=int(input("Enter Number of Students Participated: "))

# lst1=[]
# lst2=[]

# for i in range(num):
#     lst1.append(str(input(f"{i+1}Enter Name: ")))
#     lst2.append(int(input("Enter wins: ")))

# dict1=dict(zip(lst1,lst2))

# dict1.pop("Pankaj")
# del dict1["Muskan"]
# print(dict1)



dict1={"Pankaj":1,"Muskan":2,"Shubham":3}

data=dict1.items()

for i in data:
    print(i)

print(data)

for i in dict1:
    print(i)

for i in dict1.keys():
    print(i)

print(dict1.values())
print(dict1.keys())
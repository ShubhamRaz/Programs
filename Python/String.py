#3. Write a program to reverse each word in a given sentence while keeping the word order intact. For example, "Hello World" should become "olleH dlroW".

String = input("Enter String: ")
NewStr=String.split(" ")
temp=[]
for i in NewStr:
    for j in i:
        temp.insert(0,j)

    for i in temp:
        print(i,end="")
    
    print(" ",end="")
    temp.clear()
        



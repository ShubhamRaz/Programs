import os

if not os.path.exists(r"F:\Programs"):
    os.makedirs(r"F:\Programs")

else:
    pass


File=open(r"F:\Programs\Marks.txt","w")
Lst=["Name","Roll","Marks","\n"]
File.writelines(Lst)

for i in range(2):
    Lst.clear()
    

    Name=str(input("Enter Name: "))
    
    Lst.insert(0,Name)
    
    
    
    Roll=int(input("Enter Roll: "))
    
    Lst.insert(1,str(Roll))
    
    Marks=int(input("Enter Marks: "))
    
    Lst.insert(2,str(Marks))
    Lst.append("\n")
    File.writelines(Lst)



    

    


   

    


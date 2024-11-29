import os

if not os.path.exists(r"F:\Programs"):
    os.makedirs(r"F:\Programs")

else:
    pass


File=open(r"F:\Programs\Marks.txt","w")
File.write("Name Roll Marks\n")

for i in range(2):
    Name=str(input("Enter Name: "))
    File.write(f"{Name} ")
    Roll=int(input("Enter Roll: "))
    File.write(f"{Roll} ")
    Marks=int(input("Enter Marks: "))
    File.write(f"{Marks}\n")

    


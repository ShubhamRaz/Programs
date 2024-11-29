import os

Location=r"F:\Programs\new"

if not os.path.exists(Location):
    os.makedirs(Location)

else:pass

File=open(r"F:\Programs\new\marks.txt","w")

for i in range(5):
    Name=str(input("Enter Name: "))
    Roll=int(input("Enter Roll: "))
    Marks=int(input("Enter Marks: "))

    File.write(f"Name- {Name}\n Roll- {Roll}\n Marks- {Marks} \n \n")

File.close()



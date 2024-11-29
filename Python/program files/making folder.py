import os

File=r"C:\Users\kumar\OneDrive\Desktop\database\New Folder"

if not os.path.exists(File):
    os.makedirs(File)
    print("New File created")

else:print("File already exist")


n=int(input("Enter Number"))
makefile=r"C:\Users\kumar\OneDrive\Desktop\database\New Folder\new"

while n>=0:
    if not os.path.exists(f"{makefile}{n}"):
        os.makedirs(f"{makefile}{n}")

    else:
        print(f"File {makefile}{n} is already exist")
    n-=1
newname=r"C:\Users\kumar\OneDrive\Desktop\database\New Folder\Pankaj"
for i in range(6):
    if os.path.exists(f"{makefile}{i}"):
        os.rename(f"{makefile}{i}",f"{newname}{i}")


import sys
import os

if not os.path.exists(r"C:\Users\kumar\OneDrive\Desktop\pk"):
    os.makedirs(r"C:\Users\kumar\OneDrive\Desktop\pk")

File=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk.txt","w")

File.write("Hello Worlds")

File.close()

File=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk.txt","r")

print(File.readlines())
# sys.stdout(File)
File.close()

File=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk.txt")
Line=File.readline()

sys.stdout.write(Line)
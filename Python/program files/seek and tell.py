import pickle

Text="Hello World I am Pankaj,\n And what up about you. Are you Okay."

fh=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk1.txt","wb")

pickle.dump(Text,fh)

fh.close()

fh=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk1.txt","rb")





print(fh.read(1),fh.tell())
print(fh.read(2),fh.tell())
print(fh.read(3),fh.tell())

fh.seek(-3,1)

print(fh.read(2),fh.tell())
print(fh.read(1),fh.tell())



fh.close()

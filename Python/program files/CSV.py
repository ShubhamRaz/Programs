import csv

fh=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk.csv","w")

Writer=csv.writer(fh)

Writer.writerow(["Pankaj","Aryan","Shubham"])

fh.close()

fh=open(r"C:\Users\kumar\OneDrive\Desktop\pk\pk.csv","r")

Read=csv.reader(fh,delimiter="|")

for i in Read:
    print(i)

print(Read)
fh.close()


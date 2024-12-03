import csv


Data = []

n = int(input("Enter number of student: "))
for i in range(n):
    Student = []
    Student.append(int(input("Enter Roll: ")))
    Student.append(input("Enter Name: "))
    Student.append(int(input("Enter Age: ")))
    Data.append(Student)
  

print(Data)

with open("Student.csv","w",newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll","Name","Age"])
    writer.writerows(Data)


# print(Name,Roll,Age)
import csv

data=[["CGPA","Marks","Placed"],[9.5,90,1],[6.5,50,0],[7.5,75,1],[6.0,55,0],[8.7,79,1]]
with open("data.csv","w",newline = "") as file:
    writer = csv.writer(file)
    writer.writerows(data)
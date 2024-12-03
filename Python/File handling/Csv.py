import csv

# Writing dictionary data to a CSV file
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Los Angeles"},
    {"Name": "Charlie", "Age": 22, "City": "Chicago"},
    {"Name": "Diana", "Age": 28, "City": "Houston"},
    {"Name": "Eve", "Age": 35, "City": "Phoenix"},
    {"Name": "Frank", "Age": 40, "City": "Philadelphia"},
    {"Name": "Grace", "Age": 27, "City": "San Antonio"},
    {"Name": "Hank", "Age": 32, "City": "San Diego"},
    {"Name": "Ivy", "Age": 29, "City": "Dallas"},
    {"Name": "Jack", "Age": 23, "City": "San Jose"}
]

with open('output.csv', mode='w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()  # Write the header row
    writer.writerows(data)

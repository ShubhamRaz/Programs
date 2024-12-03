import matplotlib.pyplot as plt

# Sample data
labels = ["Category A", "Category B", "Category C", "Category D"]
sizes = [25, 35, 20, 20]
colors = ["gold", "lightblue", "lightcoral", "yellowgreen"]
explode = (0, 0.1, 0, 0)  # "explode" the first slice

# Create pie chart
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# Add title
plt.title("Pie Chart Example")

# Show the plot
plt.show()

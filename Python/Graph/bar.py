import matplotlib.pyplot as plt

# Sample data
categories = ["A", "B", "C", "D"]
values = [10, 15, 7, 12]

# Create bar chart
plt.bar(categories, values, color='orange')

# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart Example")

# Show the plot
plt.show()

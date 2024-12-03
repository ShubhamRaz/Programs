import matplotlib.pyplot as plt

# Sample data
x = [1, 3, 8, 10, 12]
y = [2,4,5,6,9]

# Create scatter plot
# plt.scatter(x, y, color='blue', label='Linear')
plt.plot(x, y, color='blue', label='Linear', linestyle = ":", marker = "s")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.legend()

# Show the plot
plt.show()

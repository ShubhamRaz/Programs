import matplotlib.pyplot as plt

# Sample data
data = [10,20,30,40,50,60,70,80,90]

# Create histogram
plt.hist(data, bins=9, color='green', edgecolor='black')

# Add labels and title
plt.xlabel("Value Ranges")
plt.ylabel("Frequency")
plt.title("Histogram Example")

# Show the plot
plt.show()

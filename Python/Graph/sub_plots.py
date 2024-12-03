import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [1, 2, 3, 4, 5]

# Create subplots
plt.subplot(2, 1, 1)  # (rows, cols, index)
plt.plot(x, y1, color="blue")
plt.title("First Plot")
plt.grid(True)


plt.subplot(2, 1, 2)
plt.plot(x, y2, color="green")
plt.title("Second Plot")

# Adjust layout and display
plt.tight_layout()
plt.grid(True)

plt.show()

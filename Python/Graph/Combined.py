import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Create plot with customizations
plt.figure(figsize=(8, 6))
plt.plot(x, y, color="purple", linestyle="-.", marker="s", markersize=8, label="Line")
plt.grid(True)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Customized Plot Example")
plt.legend()

# Save and display
plt.savefig("custom_plot.png")
plt.show()

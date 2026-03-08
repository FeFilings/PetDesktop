import matplotlib.pyplot as plt
import numpy as np

# Define your data points
xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

# Plot the points
plt.plot(xpoints, ypoints)

# Add labels and a title (optional but recommended)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Simple Line Graph")

# Display the graph
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Number of random points
N = 100000  # Increase N for better accuracy

# Generate random (x, y) points in the unit square [0,1] × [0,1]
x_random = np.random.uniform(0, 1, N)
y_random = np.random.uniform(0, 1, N)

# Check if points are inside the quarter-circle (x^2 + y^2 ≤ 1)
inside_circle = x_random**2 + y_random**2 <= 1

# Count points inside the quarter-circle
M = np.sum(inside_circle)

# Estimate the value of π
pi_estimate = 4 * (M / N)
# Print results
print(f"Estimated π: {pi_estimate}")
print(f"Actual π: {np.pi}")
print(f"Error: {abs(pi_estimate - np.pi)}")

# Visualization
plt.figure(figsize=(6, 6))
plt.scatter(x_random, y_random, color='blue', s=1, alpha=0.3, label="Random Points")  # All random points
plt.scatter(x_random[inside_circle], y_random[inside_circle], color='green', s=1, alpha=0.3, label="Inside Circle")  # Points inside the quarter-circle

# Draw quarter-circle boundary
circle = plt.Circle((0, 0), 1, color='red', fill=False, linewidth=2)
plt.gca().add_patch(circle)

# Draw square boundary
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.axhline(y=0, color='black', linewidth=1)
plt.axvline(x=0, color='black', linewidth=1)
plt.axhline(y=1, color='black', linestyle='dashed', linewidth=1)
plt.axvline(x=1, color='black', linestyle='dashed', linewidth=1)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Monte Carlo Estimation of π")
plt.legend()
plt.show()



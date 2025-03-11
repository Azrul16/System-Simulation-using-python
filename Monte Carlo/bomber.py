import random
import numpy as np
from tabulate import tabulate

# Constants
mu_x, mu_y = 0, 0  # Mean (center of depot)
sigma_x, sigma_y = 500, 300  # Standard deviation
num_bombs = 20  # Number of bombs

# Store results
results = []

for i in range(1, num_bombs + 1):
    # Generate normal random numbers
    z_x = np.random.normal(0, 1)
    z_y = np.random.normal(0, 1)

    # Compute strike coordinates
    x = mu_x + sigma_x * z_x
    y = mu_y + sigma_y * z_y

    # Determine hit or miss
    result = "Hit" if (-500 <= x <= 500) and (-300 <= y <= 300) else "Miss"

    # Store in results list
    results.append([i, round(z_x, 2), round(x, 2), round(z_y, 2), round(y, 2), result])

# Print table
headers = ["Bomb Strike", "RNN (z_x)", "x (m)", "RNN (z_y)", "y (m)", "Result"]
print("\nSimulation of Bombing Operation:\n")
print(tabulate(results, headers=headers, tablefmt="grid"))

# Compute and print hit percentage
hits = sum(1 for r in results if r[-1] == "Hit")
hit_percentage = (hits / num_bombs) * 100
print(f"\nTotal Hits {hits}\nTotal miss {num_bombs-hits} \nOut of {num_bombs}")
print(f"Hit Percentage: {hit_percentage:.2f}%")

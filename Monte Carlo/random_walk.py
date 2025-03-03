import numpy as np
import matplotlib.pyplot as plt
import time

# Take user input for the number of steps
steps = int(input("Enter the number of steps for the random walk: "))

# Initialize starting position
x, y = 0, 0

# Store the path for visualization
x_path, y_path = [x], [y]

# Print table header
print(f"\n{'Step':<6} {'Random Number':<15} {'Direction':<10} {'Position (x,y)':<15}")
print("=" * 50)

# Set up the figure for live updating
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots(figsize=(6, 6))

# Perform the random walk
for step in range(1, steps + 1):
    rand_num = np.random.randint(0, 10)  # Generate a random number (0 to 9)

    # Determine movement based on the random number
    if rand_num in [0, 1, 2, 3, 4]:  # Move Forward
        direction = "Forward"
        y += 1
    elif rand_num in [5, 6, 7]:  # Move Left
        direction = "Left"
        x -= 1
    else:  # Move Right (8,9)
        direction = "Right"
        x += 1

    # Store path
    x_path.append(x)
    y_path.append(y)

    # Print step details in table format
    print(f"{step:<6} {rand_num:<15} {direction:<10} ({x}, {y})")

    # Plot the updated graph
    ax.clear()
    ax.plot(x_path, y_path, marker='o', linestyle='-', markersize=4, label="Random Walk Path")
    ax.scatter([0], [0], color='green', s=100, label="Start (0,0)")  # Start position
    ax.scatter([x], [y], color='red', s=100, label=f"Step {step} ({x},{y})")  # Current position
    ax.set_xlabel("X Position")
    ax.set_ylabel("Y Position")
    ax.set_title(f"Random Walk - Step {step}/{steps}")
    ax.axhline(y=0, color='black', linewidth=1)
    ax.axvline(x=0, color='black', linewidth=1)
    ax.legend()
    ax.grid()

    plt.draw()
    plt.pause(0.5)  # Pause for animation effect

# Keep the final plot open
plt.ioff()
plt.show()

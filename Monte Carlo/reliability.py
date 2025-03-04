import random
import os
import pickle
from tabulate import tabulate

# File to store previous simulation data
SAVE_FILE = "simulation_state.pkl"

# Define probability distributions for bearing life
bearing_life_distribution = [
    (1000, 0.10), (1100, 0.14), (1200, 0.24), (1300, 0.14), (1400, 0.12),
    (1500, 0.10), (1600, 0.06), (1700, 0.05), (1800, 0.03), (1900, 0.02)
]

# Compute cumulative probabilities and random number ranges
cumulative_prob = 0
bearing_ranges = []
bearing_table = []

for life, prob in bearing_life_distribution:
    low = int(cumulative_prob * 100)
    cumulative_prob += prob
    high = int(cumulative_prob * 100) - 1
    bearing_ranges.append((low, high))
    bearing_table.append([life, prob, cumulative_prob, f"{low:02}-{high:02}"])

# Delay time probability distribution
delay_distribution = [(4, 0.3), (6, 0.6), (8, 0.1)]
delay_cumulative_prob = 0
delay_ranges = []
delay_table = []

for delay, prob in delay_distribution:
    low = int(delay_cumulative_prob * 10)
    delay_cumulative_prob += prob
    high = int(delay_cumulative_prob * 10) - 1
    delay_ranges.append((low, high))
    delay_table.append([delay, prob, delay_cumulative_prob, f"{low}-{high}"])

# Display Bearing Life Probability Table
print("\nBearing Life Probability Distribution:")
print(tabulate(bearing_table, headers=["Bearing Life (Hrs.)", "Probability", "Cumulative Probability", "Random Range"], tablefmt="grid"))

# Display Delay Time Probability Table
print("\nDelay Time Probability Distribution:")
print(tabulate(delay_table, headers=["Delay (Minutes)", "Probability", "Cumulative Probability", "Random Range"], tablefmt="grid"))

# Load previous state if it exists
if os.path.exists(SAVE_FILE):
    with open(SAVE_FILE, "rb") as file:
        previous_data = pickle.load(file)
    cumulative_life = previous_data["cumulative_life"]
    total_delay = previous_data["total_delay"]
    total_bearing_replacements = previous_data["total_bearing_replacements"]
    table_data = previous_data["table_data"]
else:
    cumulative_life = 0  # Start fresh if no previous data exists
    total_delay = 0
    total_bearing_replacements = 0
    table_data = []

# Function to get bearing life from random number
def get_bearing_life(rand_num):
    for i, (life, _) in enumerate(bearing_life_distribution):
        low, high = bearing_ranges[i]
        if low <= rand_num <= high:
            return life
    return 1000  # Default case

# Function to get delay from random number
def get_delay(rand_num):
    for i, (delay, _) in enumerate(delay_distribution):
        low, high = delay_ranges[i]
        if low <= rand_num <= high:
            return delay
    return 6  # Default case

# Simulation Parameters
num_iterations = 23  # Continue for 23 more iterations

for i in range(num_iterations):
    # Generate random numbers
    rand_b1, rand_b2, rand_b3 = random.randint(0, 99), random.randint(0, 99), random.randint(0, 99)
    rand_delay = random.randint(0, 9)

    # Determine bearing lives
    b1_life = get_bearing_life(rand_b1)
    b2_life = get_bearing_life(rand_b2)
    b3_life = get_bearing_life(rand_b3)

    # Determine first failure
    first_failure = min(b1_life, b2_life, b3_life)

    # Update cumulative life
    cumulative_life += first_failure

    # Get repair delay
    delay_minutes = get_delay(rand_delay)

    # Store results
    table_data.append([b1_life, b2_life, b3_life, first_failure, cumulative_life, rand_delay, delay_minutes])

    # Update totals
    total_delay += delay_minutes
    total_bearing_replacements += 3  # All three bearings replaced

# Save the current state for future runs
save_data = {
    "cumulative_life": cumulative_life,
    "total_delay": total_delay,
    "total_bearing_replacements": total_bearing_replacements,
    "table_data": table_data
}
with open(SAVE_FILE, "wb") as file:
    pickle.dump(save_data, file)

# Display Simulation Table
print("\nSimulation Results:")
headers = ["Bearing 1 Life (Hrs.)", "Bearing 2 Life (Hrs.)", "Bearing 3 Life (Hrs.)", "First Failure (Hrs.)",
           "Cumulated Life (Hrs.)", "RD", "Delay (Minutes)"]
print(tabulate(table_data, headers=headers, tablefmt="grid"))

# Additional Calculations
replacement_time_per_set = 40  # Minutes per replacement set
total_replacement_time = total_bearing_replacements // 3 * replacement_time_per_set
total_downtime = total_delay + total_replacement_time

# Summary Output
print("\nSummary of Simulation:")
print(f"Total Delay Time: {total_delay} minutes")
print(f"Total Bearing Replacements: {total_bearing_replacements}")
print(f"Total Replacement Time: {total_replacement_time} minutes")
print(f"Total Downtime: {total_downtime} minutes")

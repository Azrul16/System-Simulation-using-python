import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt
import time
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tabulate import tabulate  # For displaying a formatted table in the terminal


def mm1_queue_simulation_live(mean_inter_arrival, mean_service_time, max_customers):
    inter_arrival_times = np.random.exponential(mean_inter_arrival, max_customers)
    service_times = np.random.exponential(mean_service_time, max_customers)

    arrival_times = np.cumsum(inter_arrival_times)
    start_times = np.zeros(max_customers)
    finish_times = np.zeros(max_customers)

    queue_delay = 0.0
    total_queue_length = 0
    server_busy_time = 0.0
    last_departure_time = 0.0

    results_table = []  # Store data for terminal output

    for i in range(max_customers):
        if i == 0:
            start_times[i] = arrival_times[i]
        else:
            start_times[i] = max(arrival_times[i], finish_times[i - 1])

        finish_times[i] = start_times[i] + service_times[i]
        queue_delay += start_times[i] - arrival_times[i]
        total_queue_length += (start_times[i] - arrival_times[i]) / mean_inter_arrival
        server_busy_time += service_times[i]
        last_departure_time = finish_times[i]

        # Append row to the table
        results_table.append([i + 1, f"{arrival_times[i]:.4f}", f"{start_times[i]:.4f}", 
                              f"{finish_times[i]:.4f}", f"{queue_delay:.4f}"])

        # Print table every 50 iterations
        if (i + 1) % 50 == 0 or i == max_customers - 1:
            print(tabulate(results_table, headers=["Customer", "Arrival", "Start", "Finish", "Queue Delay"], 
                           tablefmt="grid"))  # Adding grid-style border
            results_table = []  # Reset table for next batch

        # Update UI every 100 iterations
        if (i + 1) % 100 == 0 or i == max_customers - 1:
            update_graph(queue_delay / (i + 1), total_queue_length / (i + 1), server_busy_time / last_departure_time,
                         last_departure_time)
            window.update()
            time.sleep(0.1)  # Simulate real-time update delay

    avg_delay_in_queue = queue_delay / max_customers
    avg_num_in_queue = total_queue_length / max_customers
    server_utilization = server_busy_time / last_departure_time
    time_simulation_ended = last_departure_time

    return {
        "Average Delay in Queue": avg_delay_in_queue,
        "Average Number in Queue": avg_num_in_queue,
        "Server Utilization": server_utilization,
        "Time Simulation Ended": time_simulation_ended
    }


def update_graph(avg_delay, avg_queue, utilization, end_time):
    ax.clear()
    labels = ["Avg Delay", "Avg Queue", "Utilization", "End Time"]
    values = [avg_delay, avg_queue, utilization, end_time]

    bars = ax.bar(labels, values, color=['#4682B4', '#32CD32', '#8A2BE2', '#FF8C00'])
    ax.set_ylabel("Values")
    ax.set_title("M/M/1 Queue Simulation Results (Live Update)")

    for bar in bars:
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{bar.get_height():.2f}", ha="center", va="bottom")

    canvas.draw()


# GUI Setup
window = tk.Tk()
window.title("M/M/1 Queue Simulation (Live)")
window.configure(bg='#F0F0F0')
window.geometry("800x600")

# Plot results
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#F0F0F0')
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.get_tk_widget().pack()

# Parameters
mean_inter_arrival = 1.0
mean_service_time = 0.8
max_customers = 500

# Run simulation
results = mm1_queue_simulation_live(mean_inter_arrival, mean_service_time, max_customers)

# Display final results
result_text = "\n".join([f"{key}: {value:.4f}" for key, value in results.items()])
result_label = tk.Label(window, text=result_text, fg='#000000', bg='#F0F0F0', font=('Arial', 12, 'bold'))
result_label.pack(pady=10)

window.mainloop()

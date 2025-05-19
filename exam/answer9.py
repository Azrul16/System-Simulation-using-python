import numpy as np
import random
from typing import List, Tuple
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation

class Customer:
    def __init__(self, arrival_time: float):
        self.arrival_time = arrival_time
        self.service_start_time = 0.0
        self.service_end_time = 0.0
        self.service_time = 0.0
        self.waiting_time = 0.0

class MM1Queue:
    def __init__(self, mean_inter_arrival_time: float, mean_service_time: float, max_customers: int):
        self.mean_inter_arrival_time = mean_inter_arrival_time
        self.mean_service_time = mean_service_time
        self.max_customers = max_customers
        self.customers: List[Customer] = []
        self.current_time = 0.0
        self.server_busy = False
        self.queue_length = 0
        self.total_waiting_time = 0.0
        self.total_service_time = 0.0
        self.total_customers_served = 0
        self.queue_history = []
        self.time_history = []
        self.server_status_history = []

    def generate_inter_arrival_time(self) -> float:
        return -self.mean_inter_arrival_time * np.log(random.random())

    def generate_service_time(self) -> float:
        return -self.mean_service_time * np.log(random.random())

    def run_simulation(self):
        next_arrival_time = self.generate_inter_arrival_time()
        next_service_end_time = float('inf')
        
        while self.total_customers_served < self.max_customers:
            if next_arrival_time < next_service_end_time:
                self.current_time = next_arrival_time
                customer = Customer(self.current_time)
                self.customers.append(customer)
                
                if not self.server_busy:
                    self.server_busy = True
                    customer.service_time = self.generate_service_time()
                    customer.service_start_time = self.current_time
                    customer.service_end_time = self.current_time + customer.service_time
                    next_service_end_time = customer.service_end_time
                else:
                    self.queue_length += 1
                
                next_arrival_time = self.current_time + self.generate_inter_arrival_time()
            else:
                self.current_time = next_service_end_time
                self.server_busy = False
                self.total_customers_served += 1
                
                if self.queue_length > 0:
                    self.queue_length -= 1
                    self.server_busy = True
                    customer = self.customers[self.total_customers_served]
                    customer.service_time = self.generate_service_time()
                    customer.service_start_time = self.current_time
                    customer.service_end_time = self.current_time + customer.service_time
                    next_service_end_time = customer.service_end_time
                else:
                    next_service_end_time = float('inf')
            
            self.queue_history.append(self.queue_length)
            self.time_history.append(self.current_time)
            self.server_status_history.append(1 if self.server_busy else 0)

        return self.calculate_statistics()

    def calculate_statistics(self):
        total_waiting_time = 0.0
        total_service_time = 0.0
        total_customers = len(self.customers)

        for customer in self.customers:
            customer.waiting_time = customer.service_start_time - customer.arrival_time
            total_waiting_time += customer.waiting_time
            total_service_time += customer.service_time

        avg_delay = total_waiting_time / total_customers
        avg_queue_length = total_waiting_time / self.current_time
        server_utilization = total_service_time / self.current_time

        return {
            'avg_delay': avg_delay,
            'avg_queue_length': avg_queue_length,
            'server_utilization': server_utilization,
            'simulation_time': self.current_time
        }

class QueueSimulationGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("M/M/1 Queue Simulation")
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.create_parameter_frame()
        self.create_plots()
        self.create_control_buttons()
        self.simulation = None
        self.animation = None

    def create_parameter_frame(self):
        param_frame = ttk.LabelFrame(self.main_frame, text="Simulation Parameters", padding="5")
        param_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        self.mean_inter_arrival = tk.DoubleVar(value=2.0)
        self.mean_service = tk.DoubleVar(value=1.5)
        self.max_customers = tk.IntVar(value=1000)
        
        ttk.Label(param_frame, text="Mean Inter-arrival Time:").grid(row=0, column=0, sticky=tk.W)
        ttk.Entry(param_frame, textvariable=self.mean_inter_arrival, width=10).grid(row=0, column=1, padx=5)
        
        ttk.Label(param_frame, text="Mean Service Time:").grid(row=1, column=0, sticky=tk.W)
        ttk.Entry(param_frame, textvariable=self.mean_service, width=10).grid(row=1, column=1, padx=5)
        
        ttk.Label(param_frame, text="Max Customers:").grid(row=2, column=0, sticky=tk.W)
        ttk.Entry(param_frame, textvariable=self.max_customers, width=10).grid(row=2, column=1, padx=5)

    def create_plots(self):
        self.fig = Figure(figsize=(10, 6))
        
        self.queue_ax = self.fig.add_subplot(211)
        self.queue_ax.set_title("Queue Length Over Time")
        self.queue_ax.set_xlabel("Time")
        self.queue_ax.set_ylabel("Queue Length")
        
        self.server_ax = self.fig.add_subplot(212)
        self.server_ax.set_title("Server Status Over Time")
        self.server_ax.set_xlabel("Time")
        self.server_ax.set_ylabel("Server Status (0=Idle, 1=Busy)")
        
        self.fig.tight_layout()
        
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.main_frame)
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, pady=5)

    def create_control_buttons(self):
        button_frame = ttk.Frame(self.main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=5)
        
        ttk.Button(button_frame, text="Run Simulation", command=self.run_simulation).grid(row=0, column=0, padx=5)
        ttk.Button(button_frame, text="Stop", command=self.stop_simulation).grid(row=0, column=1, padx=5)

    def run_simulation(self):
        self.simulation = MM1Queue(
            self.mean_inter_arrival.get(),
            self.mean_service.get(),
            self.max_customers.get()
        )
        
        import threading
        thread = threading.Thread(target=self.run_simulation_thread)
        thread.start()

    def run_simulation_thread(self):
        stats = self.simulation.run_simulation()
        
        self.queue_ax.clear()
        self.server_ax.clear()
        
        self.queue_ax.plot(self.simulation.time_history, self.simulation.queue_history)
        self.server_ax.plot(self.simulation.time_history, self.simulation.server_status_history)
        
        self.queue_ax.set_title("Queue Length Over Time")
        self.queue_ax.set_xlabel("Time")
        self.queue_ax.set_ylabel("Queue Length")
        
        self.server_ax.set_title("Server Status Over Time")
        self.server_ax.set_xlabel("Time")
        self.server_ax.set_ylabel("Server Status (0=Idle, 1=Busy)")
        
        self.fig.tight_layout()
        self.canvas.draw()
        
        self.show_statistics(stats)

    def show_statistics(self, stats):
        stats_window = tk.Toplevel(self.root)
        stats_window.title("Simulation Results")
        
        ttk.Label(stats_window, text="M/M/1 Queue Simulation Results").grid(row=0, column=0, columnspan=2, pady=5)
        ttk.Label(stats_window, text="-" * 40).grid(row=1, column=0, columnspan=2)
        
        ttk.Label(stats_window, text=f"Mean Inter-arrival Time: {self.mean_inter_arrival.get():.2f}").grid(row=2, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Mean Service Time: {self.mean_service.get():.2f}").grid(row=3, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Number of Customers: {self.max_customers.get()}").grid(row=4, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Simulation Time: {stats['simulation_time']:.2f}").grid(row=5, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Average Delay in Queue: {stats['avg_delay']:.2f}").grid(row=6, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Average Number in Queue: {stats['avg_queue_length']:.2f}").grid(row=7, column=0, columnspan=2, sticky=tk.W)
        ttk.Label(stats_window, text=f"Server Utilization: {stats['server_utilization']:.2%}").grid(row=8, column=0, columnspan=2, sticky=tk.W)

    def stop_simulation(self):
        if self.animation:
            self.animation.event_source.stop()

def main():
    root = tk.Tk()
    app = QueueSimulationGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
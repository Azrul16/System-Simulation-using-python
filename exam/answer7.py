import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from tabulate import tabulate

class CircularChessSimulation:
    def __init__(self, n_entities, max_steps=1000, dt=0.01):
        self.n_entities = n_entities
        self.max_steps = max_steps
        self.dt = dt
        self.convergence_threshold = 1e-3
        
        angles = np.linspace(0, 2*np.pi, n_entities, endpoint=False)
        self.positions = np.column_stack((np.cos(angles), np.sin(angles)))
        
        self.history = [self.positions.copy()]
        
    def update_positions(self):
        next_positions = np.roll(self.positions, -1, axis=0)
        directions = next_positions - self.positions
        
        distances = np.linalg.norm(directions, axis=1)
        directions = directions / distances[:, np.newaxis]
        self.positions += directions * self.dt
        
        self.history.append(self.positions.copy())
        
    def check_convergence(self):
        distances = np.linalg.norm(self.positions - self.positions[0], axis=1)
        max_distance = np.max(distances)
        return max_distance < self.convergence_threshold, max_distance
        
    def display_iteration_table(self, step, max_distance=None):
        table_data = []
        for i in range(self.n_entities):
            pos = self.positions[i]
            angle = np.arctan2(pos[1], pos[0])
            if angle < 0:
                angle += 2 * np.pi
            angle_deg = np.degrees(angle)
            table_data.append([f"Node {i+1}", f"({pos[0]:.4f}, {pos[1]:.4f})", f"{angle_deg:.2f}°"])
        
        print(f"\nIteration {step}:")
        if max_distance is not None:
            print(f"Maximum distance between nodes: {max_distance:.6f}")
        print(tabulate(table_data, headers=["Node", "Position (x, y)", "Angle"], tablefmt="grid"))
        
    def run_simulation(self):
        step = 0
        print("\nStarting simulation...")
        print(f"Convergence threshold: {self.convergence_threshold}")
        self.display_iteration_table(step)
        
        while step < self.max_steps:
            self.update_positions()
            converged, max_distance = self.check_convergence()
            
            if converged:
                print(f"\nConvergence achieved at step {step}!")
                print(f"Final maximum distance between nodes: {max_distance:.6f}")
                break
                
            step += 1
            if step % 10 == 0:
                self.display_iteration_table(step, max_distance)
            
        if step >= self.max_steps:
            print(f"\nMaximum iterations ({self.max_steps}) reached without convergence")
            print(f"Final maximum distance between nodes: {max_distance:.6f}")
            
        return step
    
    def animate(self):
        history = np.array(self.history)
        
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-1.2, 1.2)
        ax.set_ylim(-1.2, 1.2)
        ax.set_aspect('equal')
        ax.grid(True)
        
        circle = plt.Circle((0, 0), 1, fill=False, linestyle='--', color='gray')
        ax.add_artist(circle)
        
        scatter = ax.scatter([], [], c='blue', s=100)
        
        def init():
            scatter.set_offsets(np.empty((0, 2)))
            return scatter,
        
        def update(frame):
            scatter.set_offsets(history[frame])
            return scatter,
        
        anim = FuncAnimation(fig, update, frames=len(history),
                           init_func=init, blit=True, interval=200)
        
        plt.title('Circular Chess Simulation')
        plt.show()

def main():
    n_entities = int(input("Enter number of entities: "))
    max_steps = int(input("Enter maximum number of steps (default 1000): ") or "1000")
    dt = float(input("Enter time step (default 0.01): ") or "0.01")
    
    sim = CircularChessSimulation(n_entities, max_steps, dt)
    steps = sim.run_simulation()
    
    print(f"\nSimulation completed in {steps} steps")
    print("Displaying animation...")
    
    sim.animate()

if __name__ == "__main__":
    main() 
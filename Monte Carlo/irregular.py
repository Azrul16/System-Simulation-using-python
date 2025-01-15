import numpy as np
import matplotlib.pyplot as plt

def is_inside_figure(x, y):
    """
    Define the irregular figure here. For demonstration, let's create a simple
    irregular shape (e.g., a quarter circle)
    """
    return (x**2 + y**2) <= 1 and x >= 0 and y >= 0

def calculate_area(num_points=1000, square_size=9):
    # Generate random points
    x = np.random.uniform(0, square_size, num_points)
    y = np.random.uniform(0, square_size, num_points)
    
    # Count points inside the figure
    points_inside = sum(1 for i in range(num_points) 
                       if is_inside_figure(x[i]/square_size, y[i]/square_size))
    
    # Calculate area
    total_square_area = square_size * square_size
    ratio = points_inside / num_points
    estimated_area = ratio * total_square_area
    
    return estimated_area, x, y, points_inside

def plot_results(x, y, square_size, points_inside, num_points):
    plt.figure(figsize=(10, 10))
    
    # Plot points, coloring them based on whether they're inside or outside
    inside_figure = [is_inside_figure(x[i]/square_size, y[i]/square_size) 
                    for i in range(len(x))]
    
    plt.scatter(x[~np.array(inside_figure)], y[~np.array(inside_figure)], 
                c='red', alpha=0.6, label='Outside')
    plt.scatter(x[np.array(inside_figure)], y[np.array(inside_figure)], 
                c='blue', alpha=0.6, label='Inside')
    
    plt.grid(True)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Monte Carlo Area Estimation\n'
              f'Points inside: {points_inside}, Total points: {num_points}\n'
              f'Ratio: {points_inside/num_points:.4f}')
    plt.legend()
    plt.show()

# Run simulation with different numbers of points
num_points_list = [50, 1000, 10000]
square_size = 9

for num_points in num_points_list:
    estimated_area, x, y, points_inside = calculate_area(num_points, square_size)
    print(f"\nNumber of points: {num_points}")
    print(f"Estimated area: {estimated_area:.2f} square units")
    print(f"Ratio of points inside: {points_inside/num_points:.4f}")
    
    # Plot the results
    plot_results(x, y, square_size, points_inside, num_points)
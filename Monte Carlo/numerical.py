import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3

def monte_carlo_integration(num_points=1000):
    # Rectangle bounds
    x_min, x_max = 2, 5  # x bounds
    y_min, y_max = 0, 140  # y bounds
    rectangle_area = (x_max - x_min) * (y_max - y_min)
    
    # Generate random points
    x = np.random.uniform(x_min, x_max, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    
    # Count points under the curve
    points_under_curve = sum(1 for i in range(num_points) 
                           if y[i] <= f(x[i]))
    
    # Calculate integral
    ratio = points_under_curve / num_points
    integral = ratio * rectangle_area
    
    return integral, x, y, points_under_curve

def plot_results(x, y, points_under_curve, num_points):
    plt.figure(figsize=(12, 8))
    
    # Plot the actual function
    x_curve = np.linspace(2, 5, 1000)
    y_curve = f(x_curve)
    plt.plot(x_curve, y_curve, 'b-', label='f(x) = x³')
    
    # Plot random points
    under_curve = [y[i] <= f(x[i]) for i in range(len(x))]
    plt.scatter(x[~np.array(under_curve)], y[~np.array(under_curve)], 
                c='red', alpha=0.6, label='Outside')
    plt.scatter(x[np.array(under_curve)], y[np.array(under_curve)], 
                c='blue', alpha=0.6, label='Inside')
    
    # Plot rectangle bounds
    plt.plot([2, 2], [0, 140], 'k-', alpha=0.5)
    plt.plot([5, 5], [0, 140], 'k-', alpha=0.5)
    plt.plot([2, 5], [140, 140], 'k-', alpha=0.5)
    plt.plot([2, 5], [0, 0], 'k-', alpha=0.5)
    
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Monte Carlo Integration of x³ from 2 to 5\n'
              f'Points under curve: {points_under_curve}, Total points: {num_points}\n'
              f'Ratio: {points_under_curve/num_points:.4f}')
    plt.legend()
    plt.show()

# Run simulations with different numbers of points
num_points_list = [1000, 10000, 100000]
exact_value = 152.25

print("Exact value of integral:", exact_value)
print("\nMonte Carlo approximations:")

for num_points in num_points_list:
    integral, x, y, points_under_curve = monte_carlo_integration(num_points)
    error = abs(integral - exact_value)
    print(f"\nNumber of points: {num_points}")
    print(f"Estimated integral: {integral:.2f}")
    print(f"Absolute error: {error:.2f}")
    print(f"Relative error: {(error/exact_value)*100:.2f}%")
    
    plot_results(x, y, points_under_curve, num_points)
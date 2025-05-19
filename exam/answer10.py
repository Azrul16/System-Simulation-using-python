import numpy as np
import matplotlib.pyplot as plt

class LinearCongruentialGenerator:
    def __init__(self, seed, multiplier, increment, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.increment = increment
        self.modulus = modulus
        self.current = seed
        self.generated_numbers = [seed]

    def generate(self, count):
        for _ in range(count - 1):
            self.current = (self.multiplier * self.current + self.increment) % self.modulus
            self.generated_numbers.append(self.current)
        return self.generated_numbers

    def plot_distribution(self):
        plt.ion()
        plt.figure(figsize=(12, 6))
        
        plt.subplot(121)
        plt.scatter(self.generated_numbers[:-1], self.generated_numbers[1:], alpha=0.5)
        plt.title('Consecutive Numbers Distribution')
        plt.xlabel('X(n)')
        plt.ylabel('X(n+1)')
        plt.grid(True)
        
        plt.subplot(122)
        plt.hist(self.generated_numbers, bins=min(50, len(set(self.generated_numbers))), 
                density=True, alpha=0.7)
        plt.title('Distribution of Generated Numbers')
        plt.xlabel('Generated Numbers')
        plt.ylabel('Frequency')
        plt.grid(True)
        
        plt.tight_layout()
        plt.draw()
        plt.pause(100)
        plt.close('all')

    def calculate_statistics(self):
        numbers = np.array(self.generated_numbers)
        return {
            'mean': np.mean(numbers),
            'variance': np.var(numbers),
            'min': np.min(numbers),
            'max': np.max(numbers)
        }

def main():
    seed = 1
    multiplier = 1664525
    increment = 1013904223
    modulus = 2**32
    
    lcg = LinearCongruentialGenerator(seed, multiplier, increment, modulus)
    numbers = lcg.generate(1000)
    
    print("First 20 generated numbers:")
    for i, num in enumerate(numbers[:20], 1):
        print(f"{num:10d}", end=" ")
        if i % 5 == 0:
            print()
    print("\n")
    
    stats = lcg.calculate_statistics()
    print("Statistics:")
    print("-" * 40)
    print(f"Mean: {stats['mean']:.2f}")
    print(f"Variance: {stats['variance']:.2f}")
    print(f"Minimum: {stats['min']}")
    print(f"Maximum: {stats['max']}")
    
    lcg.plot_distribution()

if __name__ == "__main__":
    main()

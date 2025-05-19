import numpy as np
import math

def additive_congruential(b, m, r0, count):
    print("Generated numbers:")
    
    sequence = []
    current = r0
    for i in range(count):
        current = (current + b) % m
        sequence.append(current)
        print(f"{current:2d}", end=" ")
        if (i+1) % 5 == 0:
            print()
    print("\n")
    return sequence

def chi_square_cdf(x, df):
    def gamma_function(x):
        return math.gamma(x)
    
    def integrand(t):
        return (t ** (df/2 - 1)) * math.exp(-t/2)
    
    n = 1000  
    h = x / n
    x_values = np.linspace(0, x, n+1)
    y_values = [integrand(t) for t in x_values]
    
    integral = h/3 * (y_values[0] + y_values[-1] + 
                     4 * sum(y_values[1:-1:2]) + 
                     2 * sum(y_values[2:-1:2]))
    
    return integral / (2 ** (df/2) * gamma_function(df/2))

def chi_square_autocorrelation_test(sequence, lag=1, alpha=0.05):
    n = len(sequence)
    if lag >= n:
        raise ValueError("Lag must be less than sequence length")
    
    pairs = list(zip(sequence[:-lag], sequence[lag:]))
    
    pair_counts = {}
    for pair in pairs:
        pair_counts[pair] = pair_counts.get(pair, 0) + 1
    
    expected_freq = n / (len(set(sequence)) ** 2)
    
    chi_square = 0
    for count in pair_counts.values():
        chi_square += ((count - expected_freq) ** 2) / expected_freq
    
    df = len(pair_counts) - 1
    
    if df > 30:
        critical_value = df + math.sqrt(2 * df) * 1.645 
    else:
        critical_value = df
        while chi_square_cdf(critical_value, df) < (1 - alpha):
            critical_value += 0.1
    
    p_value = 1 - chi_square_cdf(chi_square, df)
    
    return {
        'chi_square': chi_square,
        'critical_value': critical_value,
        'p_value': p_value,
        'is_random': chi_square <= critical_value
    }

def main():
    count = int(input("How many numbers to generate? "))
    r0 = int(input("Initial value (r0): "))
    m = int(input("Modulus (m): "))
    b = int(input("Increment (b): "))
    
    sequence = additive_congruential(b, m, r0, count)
    
    
    test_results = chi_square_autocorrelation_test(sequence)
    
    print(f"Chi-square statistic: {test_results['chi_square']:.4f}")
    print(f"\nConclusion: The sequence is {'random' if test_results['is_random'] else 'not random'} at 5% significance level")
    

if __name__ == "__main__":
    main()
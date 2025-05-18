def ks_uniformity_test(data):
    n = len(data)
    sorted_data = sorted(data)
    
    D_plus = max((i+1)/n - sorted_data[i] for i in range(n))
    D_minus = max(sorted_data[i] - i/n for i in range(n))
    
    D = max(D_plus, D_minus)
    
    critical_value = 0.410
    
    is_uniform = D <= critical_value
    
    return D, is_uniform

data = [0.24, 0.89, 0.11, 0.61, 0.23, 0.86, 0.41, 0.64, 0.50, 0.65]

D, uniform = ks_uniformity_test(data)

print(f"D statistic: {D:.3f}")
print(f"Critical value: 0.410")
print(f"Uniform at 95% confidence: {'Yes' if uniform else 'No'}")
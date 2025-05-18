def chi_square_uniformity_test(data):
    num_classes = 10
    n = len(data)
    expected = n / num_classes
    class_width = 100 / num_classes
    
    observed = [0] * num_classes
    
    for num in data:
        class_index = min(int(num / class_width), num_classes - 1)
        observed[class_index] += 1
    
    chi_square = sum((o - expected)**2 / expected for o in observed)
    
    critical_value = 16.92
    
    is_uniform = chi_square <= critical_value
    
    return chi_square, critical_value, is_uniform, observed

data = [
    36, 91, 51, 2, 54, 6, 58, 8, 8, 2, 54, 1, 48, 97, 43, 22, 83, 25, 79, 95,
    42, 87, 73, 17, 2, 42, 95, 38, 79, 29, 65, 69, 55, 97, 39, 83, 31, 77, 17, 62,
    3, 49, 90, 37, 13, 17, 58, 11, 51, 92, 33, 78, 21, 66, 9, 54, 49, 90, 35, 84,
    26, 74, 22, 62, 12, 90, 36, 83, 32, 75, 51, 94, 34, 87, 40, 7, 58, 5, 56, 22,
    58, 77, 71, 10, 73, 23, 57, 13, 56, 89, 22, 68, 2, 44, 99, 27, 81, 26, 85
]

chi_square, critical_value, is_uniform, observed = chi_square_uniformity_test(data)

print("Class Intervals\tObserved\tExpected")
for i in range(10):
    lower = i * 10
    upper = (i + 1) * 10
    print(f"{lower}-{upper}\t\t{observed[i]}\t\t{len(data)/10:.1f}")

print(f"\nChi-square statistic: {chi_square:.2f}")
print(f"Critical value (α=0.05): {critical_value:.2f}")
print(f"Uniform at 95% confidence? {'Yes' if is_uniform else 'No'}")
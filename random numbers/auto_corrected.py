def autocorrelation_test(data):
    n = len(data)
    num_pairs = n - 1
    expected = num_pairs / 9 
    
    counts = [[0]*3 for _ in range(3)]
    
    for i in range(num_pairs):
        r1 = data[i] / 100
        r2 = data[i+1] / 100
        
        c1 = 0 if r1 <= 0.33 else 1 if r1 <= 0.67 else 2
        c2 = 0 if r2 <= 0.33 else 1 if r2 <= 0.67 else 2
        
        counts[c1][c2] += 1
    
    chi_square = 0
    for row in counts:
        for count in row:
            chi_square += (count - expected)**2 / expected
    
    critical_value = 12.592
    is_random = chi_square <= critical_value
    
    return counts, chi_square, is_random


data = [
    49,55,52,19,41,31,12,53,62,40,87,83,26,1,91,55,38,75,90,35,
    71,57,27,85,52,8,35,57,88,38,77,86,29,18,9,96,58,22,8,93,
    85,45,79,68,20,11,78,93,21,13,6,32,63,79,54,67,35,18,81,40,
    62,13,76,74,76,45,29,36,80,78,95,25,52
]

counts, chi_square, is_random = autocorrelation_test(data)


print(f"Number of pairs: {len(data)-1}")
print(f"Expected count per cell: {(len(data)-1)/9:.1f}")
print(f"Chi-square value: {chi_square:.1f}")
print(f"Critical value: 12.6")
print(f"Are numbers independent? {'Yes' if is_random else 'No'}")

print("\nObserved Counts Matrix:")
print("       R2 ≤0.33 R2 ≤0.67 R2 ≤1.00")
print("       -------- -------- --------")
for i, row in enumerate(counts):
    label = "R1 ≤0.33" if i == 0 else "R1 ≤0.67" if i == 1 else "R1 ≤1.00"
    print(f"{label} |", end="")
    for count in row:
        print(f"   {count:3d}   ", end="")
    print()
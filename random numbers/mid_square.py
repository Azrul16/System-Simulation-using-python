seed = int(input("Enter the value of seed: "))
print("Number of random numbers to be generated n=", end='')
n = int(input())

for _ in range(n):
    squared = seed * seed
    squared_str = f"{squared:08d}"
    middle = squared_str[2:6]
    seed = int(middle)
    print(f" {seed:04d} ", end='') 

print()
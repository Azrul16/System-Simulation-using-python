def mixed_multiplicative_congruential(a, b, m, r0, count):
    print("\nMixed Multiplicative Congruential Method:")
    print(f"Parameters: a={a}, b={b}, m={m}, seed={r0}")
    print("Generated numbers:")
    
    current = r0
    for i in range(count):
        current = (a * current + b) % m
        print(f"r_{i+1} = {current:2d}", end=" | ")
        if (i+1) % 5 == 0:
            print()
    print("\n")

def multiplicative_congruential(a, m, r0, count):
    print("\nMultiplicative Congruential Method:")
    print(f"Parameters: a={a}, m={m}, seed={r0}")
    print("Generated numbers:")
    
    current = r0
    for i in range(count):
        current = (a * current) % m
        print(f"r_{i+1} = {current:2d}", end=" | ")
        if (i+1) % 5 == 0:
            print()
    print("\n")

def additive_congruential(b, m, r0, count):
    print("\nAdditive Congruential Method:")
    print(f"Parameters: b={b}, m={m}, seed={r0}")
    print("Generated numbers:")
    
    current = r0
    for i in range(count):
        current = (current + b) % m
        print(f"r_{i+1} = {current:2d}", end=" | ")
        if (i+1) % 5 == 0:
            print()
    print("\n")

def main():
    print("Random Number Generator Methods:")
    print("1. Mixed Multiplicative Congruential")
    print("2. Multiplicative Congruential")
    print("3. Additive Congruential")
    
    choice = int(input("Select method (1-3): "))
    count = int(input("How many numbers to generate? "))
    r0 = int(input("Enter seed value (r0): "))
    m = int(input("Enter modulus (m): "))
    
    if choice == 1:
        a = int(input("Enter multiplier (a): "))
        b = int(input("Enter increment (b): "))
        mixed_multiplicative_congruential(a, b, m, r0, count)
    elif choice == 2:
        a = int(input("Enter multiplier (a): "))
        multiplicative_congruential(a, m, r0, count)
    elif choice == 3:
        b = int(input("Enter increment (b): "))
        additive_congruential(b, m, r0, count)
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
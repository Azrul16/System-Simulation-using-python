def arithmetic_congruential(r1, r2, m, count):
    sequence = [r1, r2]
    
    for i in range(2, count):
        next_num = (sequence[i-2] + sequence[i-1]) % m
        sequence.append(next_num)
    
    return sequence
if __name__ == "__main__":
    r1 = 9
    r2 = 13
    m = 17
    count = 20 
    sequence = arithmetic_congruential(r1, r2, m, count)

    print("Arithmetic Congruential Generator")
    print(f"Parameters: r1={r1}, r2={r2}, m={m}\n")
    print("Generated sequence:")
    
    for i, num in enumerate(sequence, 1):
        print(f"r_{i} = {num:2d}", end=" | ")
        if i % 5 == 0: 
            print()
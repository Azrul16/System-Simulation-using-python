import random

def gambling_game_simulation(num_trials):
    print(f"{'Game':<6} {'Sl. No.':<8} {'Random':<8} {'Head or Tail':<12} {'Cumulative Heads':<18} {'Tails':<8} {'Difference':<10}")
    print("-" * 80)

    total_wins = 0
    total_losses = 0

    for trial in range(1, num_trials + 1):
        heads = 0
        tails = 0
        flips = 0
        outcome = ""

        for flip in range(1, 9):  # Maximum 8 flips
            flips += 1
            random_number = random.randint(0, 9)  # Random number (0-9)
            coin_flip = "H" if random_number < 5 else "T"

            if coin_flip == "H":
                heads += 1
            else:
                tails += 1

            difference = abs(heads - tails)
            print(f"{trial:<6} {flip:<8} {random_number:<8} {coin_flip:<12} {heads:<18} {tails:<8} {difference:<10}")

            if difference == 3:
                outcome = "Win"
                total_wins += 1
                break
        else:
            outcome = "Lose"
            total_losses += 1

        # Print the outcome of the trial
        if outcome == "Win":
            print(f"{'':<6} {'':<8} {'':<8} {'':<12} {'Win Re. 1':<18}")
        else:
            print(f"{'':<6} {'':<8} {'':<8} {'':<12} {'Lose Re. 1':<18}")
        print("-" * 80)

    # Final result summary
    print("\nFinal Result Summary")
    print("-" * 40)
    print(f"Total Games Played: {num_trials}")
    print(f"Total Wins: {total_wins}")
    print(f"Total Losses: {total_losses}")
    net_earnings = total_wins - total_losses
    print(f"Net Earnings: BDT. {net_earnings}")
    print("-" * 40)

# Parameters
num_trials = int(input("Enter the number of games to simulate: "))

# Run the simulation
gambling_game_simulation(num_trials)

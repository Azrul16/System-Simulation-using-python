def poker_test(observed_counts, alpha=0.01):
    """
    Perform Poker Test on random numbers
    
    Parameters:
        observed_counts: Dictionary of observed counts for each hand type
        alpha: Significance level (default 0.01)
        
    Returns:
        chi_square: Calculated chi-square statistic
        critical_value: Critical value from chi-square distribution
        is_independent: Test result (True if numbers appear independent)
    """
    # Expected probabilities for 5-digit numbers
    probabilities = {
        'five_different': 0.3024,
        'one_pair': 0.5040,
        'two_pairs': 0.1080,
        'three_kind': 0.0720,
        'full_house': 0.0090,
        'four_kind': 0.0045,
        'five_kind': 0.0001
    }
    
    total_numbers = sum(observed_counts.values())
    
    # Calculate expected counts
    expected_counts = {k: v * total_numbers for k, v in probabilities.items()}
    
    # Calculate chi-square statistic
    chi_square = 0
    for hand in observed_counts:
        o = observed_counts[hand]
        e = expected_counts[hand]
        chi_square += (o - e)**2 / e
    
    # Critical value for 6 degrees of freedom at alpha=0.01
    critical_value = 16.8
    is_independent = chi_square <= critical_value
    
    return chi_square, critical_value, is_independent, expected_counts

# Observed counts from the example
observed = {
    'five_different': 3075,
    'one_pair': 4935,
    'two_pairs': 1135,
    'three_kind': 695,
    'full_house': 105,
    'four_kind': 54,
    'five_kind': 1
}

# Perform the test
chi_sq, crit_val, is_indep, expected = poker_test(observed)

# Print results
print("Poker Test Results")
print("==================")
print(f"Total numbers: {sum(observed.values())}")
print("\nHand Type           Observed  Expected  (O-E)²/E")
print("--------------------------------------------")
print(f"Five different    {observed['five_different']:7d}  {expected['five_different']:7.1f}  {((observed['five_different']-expected['five_different'])**2/expected['five_different']):7.4f}")
print(f"One pair          {observed['one_pair']:7d}  {expected['one_pair']:7.1f}  {((observed['one_pair']-expected['one_pair'])**2/expected['one_pair']):7.4f}")
print(f"Two pairs         {observed['two_pairs']:7d}  {expected['two_pairs']:7.1f}  {((observed['two_pairs']-expected['two_pairs'])**2/expected['two_pairs']):7.4f}")
print(f"Three of a kind   {observed['three_kind']:7d}  {expected['three_kind']:7.1f}  {((observed['three_kind']-expected['three_kind'])**2/expected['three_kind']):7.4f}")
print(f"Full house        {observed['full_house']:7d}  {expected['full_house']:7.1f}  {((observed['full_house']-expected['full_house'])**2/expected['full_house']):7.4f}")
print(f"Four of a kind    {observed['four_kind']:7d}  {expected['four_kind']:7.1f}  {((observed['four_kind']-expected['four_kind'])**2/expected['four_kind']):7.4f}")
print(f"Five of a kind    {observed['five_kind']:7d}  {expected['five_kind']:7.1f}  {((observed['five_kind']-expected['five_kind'])**2/expected['five_kind']):7.4f}")

print("\nTest Statistics")
print("--------------")
print(f"Chi-square value: {chi_sq:.4f}")
print(f"Critical value (α=0.01): {crit_val:.1f}")
print(f"Numbers appear independent? {'Yes' if is_indep else 'No'}")
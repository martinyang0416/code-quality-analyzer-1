from collections import defaultdict

def count_balanced_substrings(s):
    balance = 0
    prefix_counts = defaultdict(int)
    prefix_counts[0] = 1  # To handle the empty prefix
    result = 0

    for char in s:
        if char == 'a':
            balance += 1
        else:
            balance -= 1

        # Add the number of times this balance was seen before to the result
        result += prefix_counts.get(balance, 0)

        # Update the count for the current balance
        prefix_count
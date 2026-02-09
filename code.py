def maxSatisfaction(satisfaction):
    satisfaction.sort()
    max_sum = 0
    total_sum = 0
    current_sum = 0
    for s in reversed(satisfaction):
        total_sum += s
        current_sum += total_sum
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
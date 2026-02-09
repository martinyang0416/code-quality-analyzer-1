def min_sum_of_lengths(arr, target):
    n = len(arr)
    if n < 2:
        return -1
    
    # Compute left array
    prefix_sum = 0
    prefix_map = {0: -1}
    left = [float('inf')] * n
    for i in range(n):
        prefix_sum += arr[i]
        needed = prefix_sum - target
        if needed in prefix_map:
            j = prefix_map[needed]
            current_length = i - j
            if i == 0:
                left[i] = current_length
            else:
                left[i] = min(left[i
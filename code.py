def maximumSum(arr):
    if not arr:
        return 0
    max_sum = arr[0]
    no_deletion_prev = arr[0]
    with_deletion_prev = float('-inf')
    
    for i in range(1, len(arr)):
        current = arr[i]
        no_deletion = max(current, no_deletion_prev + current)
        with_deletion = max(no_deletion_prev, with_deletion_prev + current)
        current_max = max(no_deletion, with_deletion)
        if current_max > max_sum:
            max_sum = current_max
        no_deletion_prev, with_d
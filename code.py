def kLengthApart(nums, k):
    prev = -float('inf')
    for i, num in enumerate(nums):
        if num == 1:
            if i - prev - 1 < k and prev != -float('inf'):
                return False
            prev = i
    return True
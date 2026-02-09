MOD = 10**9 + 7

def kConcatenationMaxSum(arr, k):
    # Compute Kadane's algorithm result for maximum subarray sum (allowing empty)
    max_kadane = current = 0
    for num in arr:
        current = max(num, current + num)
        max_kadane = max(max_kadane, current)
    
    total_sum = sum(arr)
    
    # Compute maximum prefix sum
    max_prefix = current = 0
    for num in arr:
        current += num
        max_prefix = max(max_prefix, current)
    
    # Compute maximum suffix sum
    ma
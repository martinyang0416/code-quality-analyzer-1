def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: sum 0 is achievable
    
    for num in nums:
        # Iterate backwards to avoid reusing the same element multiple times
        for j in range(target, num - 1, -1):
            if dp[j - num]:
                dp[j] = True
            if dp[target]:
                return True  # Early exit if target is foun
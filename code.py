def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1  # Base case: one way to reach sum 0 (using no numbers)
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]

# The function calculates the number of combinations (with order) that sum to the target using dynamic programming.
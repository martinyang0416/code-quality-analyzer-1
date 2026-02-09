MOD = 10**9 + 7

def numSubseq(nums, target):
    nums.sort()
    n = len(nums)
    power = [1] * (n + 1)
    for i in range(1, n + 1):
        power[i] = (power[i-1] * 2) % MOD
    
    total = 0
    for j in range(n):
        left, right = 0, j
        i_max = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] + nums[j] <= target:
                i_max = mid
                left = mid + 1
            else:
                right = mid - 1
        sum_
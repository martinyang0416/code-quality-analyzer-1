def maxNonOverlappingSubarrays(nums, target):
    count = 0
    current_sum = 0
    start = 0
    n = len(nums)
    for end in range(n):
        current_sum += nums[end]
        # Adjust start to ensure current_sum doesn't exceed target
        while current_sum > target and start <= end:
            current_sum -= nums[start]
            start += 1
        # Check if current_sum matches target
        if current_sum == target:
            count += 1
            # Reset for next subarray
       
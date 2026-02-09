def longestSubarray(nums):
    sum_ones = sum(nums)
    if sum_ones == 0:
        return 0
    max_len = 0
    left = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        current_len = right - left + 1
        if current_len > max_len:
            max_len = current_len
    return max_len - 1 if max_len > 0 else 0
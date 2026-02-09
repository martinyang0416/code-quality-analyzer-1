import collections

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        max_deque = collections.deque()
        min_deque = collections.deque()
        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            # Maintain max_deque for current window's max
            while max_deque and nums[right] >= nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)
            
            # Maintain mi
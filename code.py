from collections import defaultdict
from typing import List

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        res = 0
        for num in A:
            prefix_sum += num
            res += count.get(prefix_sum - S, 0)
            count[prefix_sum] += 1
        return res
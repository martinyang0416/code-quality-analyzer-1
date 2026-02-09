from typing import List

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        n = len(A)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i+1] = prefix[i] + A[i]
        
        deque = []
        deque.append(0)
        min_len = float('inf')
        
        for j in range(1, len(prefix)):
            # Maintain deque to keep prefix in increasing order
            while deque and prefix[j] <= prefix[deque[-1]]:
                deque.
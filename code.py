from typing import List
from collections import deque

class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        rows = len(A)
        if rows == 0:
            return 0
        cols = len(A[0])
        q = deque()
        
        # Collect all perimeter land cells and start BFS from them
        for i in range(rows):
            for j in range(cols):
                if (i == 0 or i == rows - 1 or j == 0 or j == cols - 1) and A[i][j] == 1:
                    q.append((i, j)
from collections import defaultdict

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        m = N.bit_length()
        len_S = len(S)
        subs = defaultdict(set)
        
        for l in range(1, m + 1):
            if l > len_S:
                continue
            for i in range(len_S - l + 1):
                sub = S[i:i+l]
                subs[l].add(sub)
        
        for l in range(1, m):
            expected = 1 << (l - 1)
            max_possible = len_S - l +